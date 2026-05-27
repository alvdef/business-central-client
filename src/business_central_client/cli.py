from __future__ import annotations

import argparse
from pathlib import Path

from business_central_client.generator.ir import DocsSnapshot
from business_central_client.generator.scraper import DEFAULT_INDEX_URL, DocsScraper
from business_central_client.generator.sdk import render_sdk

DEFAULT_IR_PATH = Path("docs/business-central-v2.ir.json")
DEFAULT_OUTPUT_PATH = Path("src/business_central_client/generated/resources.py")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="bc-client")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scrape_parser = subparsers.add_parser("scrape", help="Scrape Microsoft Learn into IR JSON")
    scrape_parser.add_argument("--index-url", default=DEFAULT_INDEX_URL)
    scrape_parser.add_argument("--ir-path", type=Path, default=DEFAULT_IR_PATH)

    generate_parser = subparsers.add_parser("generate", help="Generate SDK methods from IR JSON")
    generate_parser.add_argument("--ir-path", type=Path, default=DEFAULT_IR_PATH)
    generate_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)

    regenerate_parser = subparsers.add_parser(
        "regenerate",
        help="Scrape docs and generate SDK methods",
    )
    regenerate_parser.add_argument("--index-url", default=DEFAULT_INDEX_URL)
    regenerate_parser.add_argument("--ir-path", type=Path, default=DEFAULT_IR_PATH)
    regenerate_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)

    args = parser.parse_args(argv)

    if args.command == "scrape":
        snapshot = _scrape(args.index_url)
        _write_text(args.ir_path, snapshot.to_json())
        print(f"Wrote {len(snapshot.endpoints)} endpoints to {args.ir_path}")
        return 0

    if args.command == "generate":
        snapshot = DocsSnapshot.from_json(args.ir_path.read_text(encoding="utf-8"))
        _write_text(args.output, render_sdk(snapshot))
        print(f"Wrote generated SDK to {args.output}")
        return 0

    if args.command == "regenerate":
        snapshot = _scrape(args.index_url)
        _write_text(args.ir_path, snapshot.to_json())
        _write_text(args.output, render_sdk(snapshot))
        print(f"Wrote {len(snapshot.endpoints)} endpoints and generated SDK")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


def _scrape(index_url: str) -> DocsSnapshot:
    with DocsScraper() as scraper:
        return scraper.scrape(index_url)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
