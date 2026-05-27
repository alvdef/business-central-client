from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

from business_central_client.generator.ir import DocsSnapshot, Endpoint
from business_central_client.generator.names import pascal_case, snake_case

CONTRACT_VERSION = 1
PYTHON_TYPE_IMPORTS = {
    "Any": "typing",
    "date": "datetime",
    "datetime": "datetime",
    "Decimal": "decimal",
    "UUID": "uuid",
}


@dataclass(frozen=True, slots=True)
class FieldContract:
    name: str
    alias: str
    type: str
    required: bool = False
    source: str = "example"
    confidence: str = "high"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FieldContract:
        return cls(
            name=str(data["name"]),
            alias=str(data["alias"]),
            type=str(data["type"]),
            required=bool(data.get("required", False)),
            source=str(data.get("source", "example")),
            confidence=str(data.get("confidence", "high")),
        )


@dataclass(frozen=True, slots=True)
class ModelContract:
    name: str
    resource: str
    purpose: str
    fields: tuple[FieldContract, ...] = ()
    docs_urls: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ModelContract:
        return cls(
            name=str(data["name"]),
            resource=str(data["resource"]),
            purpose=str(data["purpose"]),
            fields=tuple(FieldContract.from_dict(item) for item in data.get("fields", [])),
            docs_urls=tuple(str(item) for item in data.get("docs_urls", [])),
        )


@dataclass(frozen=True, slots=True)
class OperationContract:
    operation_id: str
    method: str
    path: str
    resource: str
    action: str
    title: str
    docs_url: str
    summary: str | None = None
    path_params: tuple[str, ...] = ()
    request_model: str | None = None
    response_model: str | None = None
    response_is_collection: bool = False
    request_example: str | None = None
    response_example: str | None = None

    @classmethod
    def from_endpoint(
        cls,
        endpoint: Endpoint,
        *,
        request_model: str | None,
        response_model: str | None,
        response_is_collection: bool,
    ) -> OperationContract:
        example = endpoint.examples[0] if endpoint.examples else None
        return cls(
            operation_id=endpoint.operation_id,
            method=endpoint.method,
            path=endpoint.path,
            resource=endpoint.resource,
            action=endpoint.action,
            title=endpoint.title,
            docs_url=endpoint.docs_url,
            summary=endpoint.summary,
            path_params=endpoint.path_params,
            request_model=request_model,
            response_model=response_model,
            response_is_collection=response_is_collection,
            request_example=example.request if example else None,
            response_example=example.response if example else None,
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> OperationContract:
        return cls(
            operation_id=str(data["operation_id"]),
            method=str(data["method"]),
            path=str(data["path"]),
            resource=str(data["resource"]),
            action=str(data["action"]),
            title=str(data["title"]),
            docs_url=str(data["docs_url"]),
            summary=_optional_str(data.get("summary")),
            path_params=tuple(str(item) for item in data.get("path_params", [])),
            request_model=_optional_str(data.get("request_model")),
            response_model=_optional_str(data.get("response_model")),
            response_is_collection=bool(data.get("response_is_collection", False)),
            request_example=_optional_str(data.get("request_example")),
            response_example=_optional_str(data.get("response_example")),
        )


@dataclass(frozen=True, slots=True)
class ContractGraph:
    source_url: str
    contract_version: int = CONTRACT_VERSION
    models: tuple[ModelContract, ...] = ()
    operations: tuple[OperationContract, ...] = ()

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_json(cls, text: str) -> ContractGraph:
        data = json.loads(text)
        return cls(
            source_url=str(data["source_url"]),
            contract_version=int(data.get("contract_version", CONTRACT_VERSION)),
            models=tuple(ModelContract.from_dict(item) for item in data.get("models", [])),
            operations=tuple(
                OperationContract.from_dict(item) for item in data.get("operations", [])
            ),
        )

    def model_by_name(self) -> dict[str, ModelContract]:
        return {model.name: model for model in self.models}


class _ModelBuilder:
    def __init__(self, name: str, resource: str, purpose: str) -> None:
        self.name = name
        self.resource = resource
        self.purpose = purpose
        self.fields: dict[str, FieldContract] = {}
        self.docs_urls: set[str] = set()

    def merge_object(
        self,
        value: dict[str, Any],
        *,
        docs_url: str,
        registry: dict[str, _ModelBuilder],
    ) -> None:
        self.docs_urls.add(docs_url)
        for alias, field_value in value.items():
            field_name = snake_case(alias)
            field_type = _infer_type(
                field_value,
                parent_model=self.name,
                field_alias=alias,
                resource=self.resource,
                purpose=self.purpose,
                docs_url=docs_url,
                registry=registry,
            )
            existing = self.fields.get(field_name)
            if existing is None:
                self.fields[field_name] = FieldContract(
                    name=field_name,
                    alias=alias,
                    type=field_type,
                    required=False,
                )
            elif existing.type != field_type:
                self.fields[field_name] = FieldContract(
                    name=existing.name,
                    alias=existing.alias,
                    type=_merge_types(existing.type, field_type),
                    required=False,
                    confidence="medium",
                )

    def build(self) -> ModelContract:
        fields = tuple(sorted(self.fields.values(), key=lambda item: item.name))
        return ModelContract(
            name=self.name,
            resource=self.resource,
            purpose=self.purpose,
            fields=fields,
            docs_urls=tuple(sorted(self.docs_urls)),
        )


def build_contract(snapshot: DocsSnapshot) -> ContractGraph:
    registry: dict[str, _ModelBuilder] = {}
    response_models_by_resource: dict[str, str] = {}
    operations: list[OperationContract] = []

    for endpoint in snapshot.all_endpoints():
        example = endpoint.examples[0] if endpoint.examples else None
        request_json = _extract_json(example.request if example else None)
        response_json = _extract_json(example.response if example else None)

        response_model = _response_model_for_endpoint(
            endpoint,
            response_json=response_json,
            registry=registry,
        )
        if response_model:
            response_models_by_resource[endpoint.resource] = response_model

        request_model = _request_model_for_endpoint(
            endpoint,
            request_json=request_json,
            registry=registry,
        )
        operations.append(
            OperationContract.from_endpoint(
                endpoint,
                request_model=request_model,
                response_model=response_model,
                response_is_collection=endpoint.action == "list",
            )
        )

    operations = _fill_collection_response_models(operations, response_models_by_resource)
    models = tuple(
        builder.build()
        for builder in sorted(registry.values(), key=lambda item: (item.name, item.purpose))
        if builder.fields
    )
    return ContractGraph(
        source_url=snapshot.source_url,
        models=models,
        operations=tuple(operations),
    )


def python_type_imports(type_expression: str) -> set[str]:
    imports: set[str] = set()
    for token in re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", type_expression):
        module = PYTHON_TYPE_IMPORTS.get(token)
        if module:
            imports.add(module)
    return imports


def _response_model_for_endpoint(
    endpoint: Endpoint,
    *,
    response_json: Any,
    registry: dict[str, _ModelBuilder],
) -> str | None:
    if endpoint.method == "DELETE":
        return None
    payload = _object_payload(response_json)
    if payload is None:
        return None
    model_name = pascal_case(endpoint.resource)
    _model_builder(registry, model_name, endpoint.resource, "response").merge_object(
        payload,
        docs_url=endpoint.docs_url,
        registry=registry,
    )
    return model_name


def _request_model_for_endpoint(
    endpoint: Endpoint,
    *,
    request_json: Any,
    registry: dict[str, _ModelBuilder],
) -> str | None:
    if endpoint.method not in {"POST", "PATCH", "PUT"}:
        return None
    payload = _object_payload(request_json)
    if payload is None:
        return None
    suffix = "Create" if endpoint.method == "POST" else "Update"
    model_name = f"{pascal_case(endpoint.resource)}{suffix}"
    _model_builder(registry, model_name, endpoint.resource, suffix.lower()).merge_object(
        payload,
        docs_url=endpoint.docs_url,
        registry=registry,
    )
    return model_name


def _fill_collection_response_models(
    operations: list[OperationContract],
    response_models_by_resource: dict[str, str],
) -> list[OperationContract]:
    filled: list[OperationContract] = []
    for operation in operations:
        if (
            operation.response_model is None
            and operation.resource in response_models_by_resource
            and operation.method != "DELETE"
        ):
            filled.append(
                OperationContract(
                    operation_id=operation.operation_id,
                    method=operation.method,
                    path=operation.path,
                    resource=operation.resource,
                    action=operation.action,
                    title=operation.title,
                    docs_url=operation.docs_url,
                    summary=operation.summary,
                    path_params=operation.path_params,
                    request_model=operation.request_model,
                    response_model=response_models_by_resource[operation.resource],
                    response_is_collection=operation.response_is_collection,
                    request_example=operation.request_example,
                    response_example=operation.response_example,
                )
            )
        else:
            filled.append(operation)
    return filled


def _infer_type(
    value: Any,
    *,
    parent_model: str,
    field_alias: str,
    resource: str,
    purpose: str,
    docs_url: str,
    registry: dict[str, _ModelBuilder],
) -> str:
    if value is None:
        return "Any"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "Decimal"
    if isinstance(value, str):
        return _infer_string_type(value)
    if isinstance(value, list):
        return _infer_list_type(
            value,
            parent_model=parent_model,
            field_alias=field_alias,
            resource=resource,
            purpose=purpose,
            docs_url=docs_url,
            registry=registry,
        )
    if isinstance(value, dict):
        nested_name = f"{parent_model}{pascal_case(field_alias)}"
        _model_builder(registry, nested_name, resource, purpose).merge_object(
            value,
            docs_url=docs_url,
            registry=registry,
        )
        return nested_name
    return "Any"


def _infer_list_type(
    values: list[Any],
    *,
    parent_model: str,
    field_alias: str,
    resource: str,
    purpose: str,
    docs_url: str,
    registry: dict[str, _ModelBuilder],
) -> str:
    if not values:
        return "list[Any]"
    item_types = {
        _infer_type(
            value,
            parent_model=parent_model,
            field_alias=field_alias,
            resource=resource,
            purpose=purpose,
            docs_url=docs_url,
            registry=registry,
        )
        for value in values
    }
    item_type = item_types.pop() if len(item_types) == 1 else "Any"
    return f"list[{item_type}]"


def _infer_string_type(value: str) -> str:
    if not value:
        return "str"
    try:
        UUID(value)
    except ValueError:
        pass
    else:
        return "UUID"
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        pass
    else:
        return "datetime" if "T" in value else "date"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return "date"
    try:
        Decimal(value)
    except Exception:
        return "str"
    return "str"


def _merge_types(left: str, right: str) -> str:
    if left == right:
        return left
    if {left, right} <= {"int", "Decimal"}:
        return "Decimal"
    if "Any" in {left, right}:
        return left if right == "Any" else right
    return "Any"


def _object_payload(value: Any) -> dict[str, Any] | None:
    if isinstance(value, dict):
        if isinstance(value.get("value"), list) and value["value"]:
            first = value["value"][0]
            return first if isinstance(first, dict) else None
        return value
    if isinstance(value, list) and value:
        first = value[0]
        return first if isinstance(first, dict) else None
    return None


def _extract_json(text: str | None) -> Any:
    if not text:
        return None
    decoder = json.JSONDecoder()
    for index, char in enumerate(text):
        if char not in "[{":
            continue
        try:
            value, _end = decoder.raw_decode(text[index:])
        except json.JSONDecodeError:
            continue
        return value
    return None


def _model_builder(
    registry: dict[str, _ModelBuilder],
    name: str,
    resource: str,
    purpose: str,
) -> _ModelBuilder:
    builder = registry.get(name)
    if builder is None:
        builder = _ModelBuilder(name, resource, purpose)
        registry[name] = builder
    return builder


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
