#!/usr/bin/env python3
"""Simple local agent that mirrors jobs from inbox to outbox."""
from __future__ import annotations

import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "jobs" / "inbox"
OUTBOX = ROOT / "jobs" / "outbox"
POLL_INTERVAL = 2


def process_job(job_path: Path) -> None:
    output = OUTBOX / f"{job_path.stem}.result.json"
    payload = {
        "job_id": job_path.stem,
        "source": str(job_path),
        "content_preview": job_path.read_text(encoding="utf-8")[:200],
        "status": "processed",
    }
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    job_path.unlink()
    print(f"processed {job_path.name} -> {output}")


def main() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    OUTBOX.mkdir(parents=True, exist_ok=True)
    print(f"agent started; watching {INBOX}")
    try:
        while True:
            for job_file in sorted(INBOX.glob("*")):
                if job_file.is_file():
                    process_job(job_file)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("agent stopped")


if __name__ == "__main__":
    main()
