#!/usr/bin/env python3
"""Minimal syscheck CLI that emits JSON describing the local environment."""
from __future__ import annotations

import argparse
import json
import logging
import platform
import socket
import sys
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("syscheck")


def collect_details() -> dict:
    logger.debug("collecting platform details")
    return {
        "collected_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "python_version": sys.version.split()[0],
        "os": platform.system(),
        "os_release": platform.release(),
        "node": socket.gethostname(),
        "arch": platform.machine(),
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Emit system details as JSON")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the JSON payload. Printed to stdout otherwise.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the JSON for readability.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity",
    )
    return parser.parse_args(argv)


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def emit(payload: dict, destination: Path | None, pretty: bool) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=True)
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text + "\n", encoding="utf-8")
        logger.info("wrote %s", destination)
    else:
        print(text)


def main() -> None:
    args = parse_args()
    configure_logging(args.log_level)
    payload = collect_details()
    emit(payload, args.output, args.pretty)


if __name__ == "__main__":
    main()
