from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ODataQuery:
    """Composable helper for common Business Central OData query options."""

    select: tuple[str, ...] = ()
    expand: tuple[str, ...] = ()
    filter: str | None = None
    orderby: tuple[str, ...] = ()
    top: int | None = None
    skip: int | None = None
    extra: Mapping[str, Any] = field(default_factory=dict)

    def to_params(self) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if self.select:
            params["$select"] = ",".join(self.select)
        if self.expand:
            params["$expand"] = ",".join(self.expand)
        if self.filter:
            params["$filter"] = self.filter
        if self.orderby:
            params["$orderby"] = ",".join(self.orderby)
        if self.top is not None:
            params["$top"] = self.top
        if self.skip is not None:
            params["$skip"] = self.skip
        params.update(self.extra)
        return params


def merge_query_params(
    query: ODataQuery | Mapping[str, Any] | None,
    params: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    if query is not None:
        if isinstance(query, ODataQuery):
            merged.update(query.to_params())
        else:
            merged.update(query)
    if params is not None:
        merged.update(params)
    return merged
