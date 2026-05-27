from __future__ import annotations

import re
from collections import defaultdict
from textwrap import indent

from business_central_client.generator.contract import ContractGraph, OperationContract
from business_central_client.generator.names import pascal_case, pluralize, snake_case

HEADER = '''from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import quote

from business_central_client.client import BusinessCentralClient
from business_central_client.generated import models as _models
from business_central_client.odata import ODataQuery


def _path_value(value: str) -> str:
    return quote(str(value), safe="")


def _body_payload(
    body: _models.BusinessCentralModel | Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if body is None:
        return None
    if isinstance(body, _models.BusinessCentralModel):
        return body.model_dump(by_alias=True, exclude_none=True)
    return body


class _EntityClient:
    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client


class BusinessCentralAPI:
    """Generated entity-scoped facade for Microsoft Dynamics 365 Business Central API v2.0."""

    def __init__(self, client: BusinessCentralClient) -> None:
        self._client = client
'''


def render_sdk(contract: ContractGraph) -> str:
    operations = sorted(
        contract.operations,
        key=lambda operation: (
            operation.resource,
            operation.action,
            operation.method,
            operation.path,
            operation.operation_id,
        ),
    )
    grouped = _group_operations(operations)

    body = HEADER
    if not grouped:
        return body + "\n"

    for resource in grouped:
        body += _render_api_property(resource)
    body += "\n"

    for resource, resource_operations in grouped.items():
        body += "\n" + _render_entity_class(resource, resource_operations)
    return body


def _group_operations(operations: list[OperationContract]) -> dict[str, list[OperationContract]]:
    grouped: dict[str, list[OperationContract]] = defaultdict(list)
    for operation in operations:
        grouped[operation.resource].append(operation)
    return dict(sorted(grouped.items()))


def _render_api_property(resource: str) -> str:
    property_name = pluralize(snake_case(resource))
    class_name = _entity_class_name(resource)
    return f'''
    @property
    def {property_name}(self) -> {class_name}:
        """Operations for ``{property_name}``."""

        return {class_name}(self._client)
'''


def _render_entity_class(resource: str, operations: list[OperationContract]) -> str:
    class_name = _entity_class_name(resource)
    body = f'''class {class_name}(_EntityClient):
    """Generated operations for ``{pluralize(snake_case(resource))}``."""
'''

    used_names: set[str] = set()
    for operation in operations:
        body += "\n" + _render_operation_method(operation, used_names)
    return body


def _render_operation_method(operation: OperationContract, used_names: set[str]) -> str:
    method_name = _method_name(operation)
    if method_name in used_names:
        method_name = f"{method_name}_{_operation_suffix(operation)}"
    used_names.add(method_name)

    signature_params = "".join(
        f"        {snake_case(param)}: str,\n" for param in operation.path_params
    )
    body_param = _body_param(operation)
    etag_param = _etag_param(operation)
    docstring = _docstring(operation)
    path_expression = _path_expression(operation.path)
    call = _client_call(operation)
    return_type = _return_type(operation)

    source = f'''    def {method_name}(
        self,
{signature_params}{body_param}        *,
        query: ODataQuery | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
{etag_param}    ) -> {return_type}:
{indent(docstring, "        ")}

        path = {path_expression}
{call}
'''
    return source


def _method_name(operation: OperationContract) -> str:
    if operation.action == "list":
        return "list"
    return snake_case(operation.action)


def _operation_suffix(operation: OperationContract) -> str:
    operation_id = snake_case(operation.operation_id)
    resource = snake_case(operation.resource)
    operation_id = operation_id.removeprefix("dynamics_")
    operation_id = operation_id.removeprefix(f"{resource}_")
    return operation_id or snake_case(operation.method.lower())


def _body_param(operation: OperationContract) -> str:
    if operation.method not in {"POST", "PATCH", "PUT"}:
        return ""
    body_type = (
        f"_models.{operation.request_model} | Mapping[str, Any] | None"
        if operation.request_model
        else "Mapping[str, Any] | None"
    )
    return f"        body: {body_type} = None,\n"


def _etag_param(operation: OperationContract) -> str:
    if operation.method in {"PATCH", "DELETE"}:
        return "        etag: str | None = None,\n"
    return ""


def _client_call(operation: OperationContract) -> str:
    if operation.method == "GET" and operation.response_is_collection:
        if operation.response_model:
            return (
                "        items = self._client.get_value(path, query=query, params=params)\n"
                f"        return [_models.{operation.response_model}.model_validate(item) "
                "for item in items]"
            )
        return "        return self._client.get_value(path, query=query, params=params)"
    if operation.method == "GET":
        if operation.response_model:
            return (
                "        data = self._client.get(path, query=query, params=params)\n"
                f"        return _models.{operation.response_model}.model_validate(data)"
            )
        return "        return self._client.get(path, query=query, params=params)"
    if operation.method == "POST":
        if operation.response_model:
            return (
                "        data = self._client.post(\n"
                "            path,\n"
                "            json=_body_payload(body),\n"
                "            query=query,\n"
                "            params=params,\n"
                "        )\n"
                f"        return _models.{operation.response_model}.model_validate(data)"
            )
        return (
            "        return self._client.post(\n"
            "            path,\n"
            "            json=_body_payload(body),\n"
            "            query=query,\n"
            "            params=params,\n"
            "        )"
        )
    if operation.method in {"PATCH", "PUT"}:
        assignment = "data = " if operation.response_model else "return "
        call = (
            f"        {assignment}self._client.patch(\n"
            "            path,\n"
            "            json=_body_payload(body),\n"
            "            query=query,\n"
            "            params=params,\n"
            "            etag=etag,\n"
            "        )"
        )
        if operation.response_model:
            return f"{call}\n        return _models.{operation.response_model}.model_validate(data)"
        return call
    if operation.method == "DELETE":
        return "        return self._client.delete(path, query=query, params=params, etag=etag)"
    return (
        f'        return self._client.request("{operation.method}", '
        "path, query=query, params=params)"
    )


def _return_type(operation: OperationContract) -> str:
    if operation.method == "DELETE":
        return "None"
    if operation.response_model and operation.response_is_collection:
        return f"list[_models.{operation.response_model}]"
    if operation.response_model:
        return f"_models.{operation.response_model}"
    if operation.method == "GET" and operation.response_is_collection:
        return "list[dict[str, Any]]"
    return "dict[str, Any]"


def _docstring(operation: OperationContract) -> str:
    lines = [f'"""{operation.title}']
    if operation.summary:
        lines.extend(["", _escape_docstring(operation.summary)])
    lines.extend(
        [
            "",
            f"HTTP method: {operation.method}",
            f"Docs: {operation.docs_url}",
            f"Operation id: {operation.operation_id}",
        ]
    )
    if operation.request_model:
        lines.append(f"Request model: {operation.request_model}")
    if operation.response_model:
        response = (
            f"list[{operation.response_model}]"
            if operation.response_is_collection
            else operation.response_model
        )
        lines.append(f"Response model: {response}")
    if operation.request_example:
        snippet = _escape_docstring(_trim_example(operation.request_example))
        lines.extend(["", "Example request:", snippet])
    if operation.response_example:
        snippet = _escape_docstring(_trim_example(operation.response_example))
        lines.extend(["", "Example response:", snippet])
    lines.append('"""')
    return "\n".join(lines)


def _path_expression(path: str) -> str:
    parts: list[str] = []
    cursor = 0
    for match in re.finditer(r"{([A-Za-z_][A-Za-z0-9_]*)}", path):
        if match.start() > cursor:
            parts.append(repr(path[cursor : match.start()]))
        parts.append(f"_path_value({snake_case(match.group(1))})")
        cursor = match.end()
    if cursor < len(path):
        parts.append(repr(path[cursor:]))
    if not parts:
        return repr(path)
    expression = " + ".join(parts)
    if len(expression) <= 80:
        return expression
    return "(\n            " + "\n            + ".join(parts) + "\n        )"


def _entity_class_name(resource: str) -> str:
    return f"{pascal_case(pluralize(resource))}Client"


def _trim_example(text: str, *, max_lines: int = 12) -> str:
    lines = [_trim_line(line.rstrip()) for line in text.strip().splitlines()]
    if len(lines) > max_lines:
        lines = [*lines[:max_lines], "..."]
    return "\n".join(lines)


def _trim_line(text: str, *, max_chars: int = 88) -> str:
    if len(text) <= max_chars:
        return text
    return f"{text[: max_chars - 3]}..."


def _escape_docstring(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', r"\"\"\"")


__all__ = ["render_sdk"]
