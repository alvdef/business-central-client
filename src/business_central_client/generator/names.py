from __future__ import annotations

import keyword
import re

RESERVED = {"filter", "select", "expand", "from", "class", "global", "async"}


def snake_case(value: str) -> str:
    value = value.replace("-", "_").replace(" ", "_")
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_").lower()
    if not value:
        value = "value"
    if value[0].isdigit():
        value = f"_{value}"
    if keyword.iskeyword(value) or value in RESERVED:
        value = f"{value}_"
    return value


def pascal_case(value: str) -> str:
    return "".join(part.capitalize() for part in snake_case(value).split("_") if part)


def singularize(value: str) -> str:
    if value.endswith("status"):
        return value
    if value.endswith("ies") and len(value) > 3:
        return f"{value[:-3]}y"
    if value.endswith("statuses"):
        return value[:-2]
    if value.endswith("s") and not value.endswith("ss"):
        return value[:-1]
    return value


def pluralize(value: str) -> str:
    if value.endswith("y"):
        return f"{value[:-1]}ies"
    if value.endswith("s"):
        return value
    return f"{value}s"
