from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from typing import Any

IR_VERSION = 1


@dataclass(frozen=True, slots=True)
class Example:
    title: str
    request: str | None = None
    response: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Example:
        return cls(
            title=str(data.get("title", "")),
            request=_optional_str(data.get("request")),
            response=_optional_str(data.get("response")),
        )


@dataclass(frozen=True, slots=True)
class Endpoint:
    operation_id: str
    method: str
    path: str
    resource: str
    action: str
    title: str
    docs_url: str
    summary: str | None = None
    examples: tuple[Example, ...] = ()

    @property
    def path_params(self) -> tuple[str, ...]:
        seen: list[str] = []
        for param in re.findall(r"{([A-Za-z_][A-Za-z0-9_]*)}", self.path):
            if param not in seen:
                seen.append(param)
        return tuple(seen)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Endpoint:
        return cls(
            operation_id=str(data["operation_id"]),
            method=str(data["method"]).upper(),
            path=str(data["path"]),
            resource=str(data["resource"]),
            action=str(data["action"]),
            title=str(data["title"]),
            docs_url=str(data["docs_url"]),
            summary=_optional_str(data.get("summary")),
            examples=tuple(Example.from_dict(item) for item in data.get("examples", [])),
        )


@dataclass(frozen=True, slots=True)
class DocsSnapshot:
    source_url: str
    scraped_at: str
    endpoints: tuple[Endpoint, ...] = field(default_factory=tuple)
    ir_version: int = IR_VERSION

    @classmethod
    def create(cls, *, source_url: str, endpoints: list[Endpoint]) -> DocsSnapshot:
        unique = {
            (endpoint.operation_id, endpoint.method, endpoint.path): endpoint
            for endpoint in endpoints
        }
        ordered = tuple(
            sorted(
                unique.values(),
                key=lambda endpoint: (endpoint.resource, endpoint.action, endpoint.path),
            )
        )
        return cls(
            source_url=source_url,
            scraped_at="not-recorded",
            endpoints=ordered,
        )

    def all_endpoints(self) -> tuple[Endpoint, ...]:
        return self.endpoints

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_json(cls, text: str) -> DocsSnapshot:
        data = json.loads(text)
        return cls(
            source_url=str(data["source_url"]),
            scraped_at=str(data["scraped_at"]),
            endpoints=tuple(Endpoint.from_dict(item) for item in data.get("endpoints", [])),
            ir_version=int(data.get("ir_version", IR_VERSION)),
        )


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
