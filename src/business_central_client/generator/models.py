from __future__ import annotations

import re

from business_central_client.generator.contract import (
    ContractGraph,
    ModelContract,
    python_type_imports,
)

HEADER = '''from __future__ import annotations

from datetime import date as Date
from datetime import datetime as DateTime
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BusinessCentralModel(BaseModel):
    """Base model for generated Business Central schemas."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")
'''


def render_models(contract: ContractGraph) -> str:
    body = HEADER
    for model in contract.models:
        body += "\n\n" + _render_model(model)
    body += "\n\n__all__ = [\n    \"BusinessCentralModel\","
    for model in contract.models:
        body += f'\n    "{model.name}",'
    body += "\n]\n"
    return body


def _render_model(model: ModelContract) -> str:
    lines = [
        f"class {model.name}(BusinessCentralModel):",
        f'    """Generated schema for ``{model.resource}`` ({model.purpose})."""',
    ]
    if not model.fields:
        lines.append("    pass")
        return "\n".join(lines)

    for field in model.fields:
        type_expr = _safe_type(field.type)
        default = "..." if field.required else "None"
        annotation = f"{field.name}: {type_expr} | None"
        if field.alias == field.name:
            lines.append(f"    {annotation} = {default}")
        elif len(f'    {annotation} = Field({default}, alias="{field.alias}")') <= 100:
            lines.append(
                f'    {annotation} = Field({default}, alias="{field.alias}")'
            )
        else:
            lines.extend(
                [
                    f"    {annotation} = Field(",
                    f"        {default},",
                    f'        alias="{field.alias}",',
                    "    )",
                ]
            )
    return "\n".join(lines)


def _safe_type(type_expression: str) -> str:
    # Keep unknown generated model references as-is, but ensure standard imported
    # types stay visible to static analyzers and linters.
    _ = python_type_imports(type_expression)
    return re.sub(r"\bdatetime\b", "DateTime", re.sub(r"\bdate\b", "Date", type_expression))


__all__ = ["render_models"]
