#!/usr/bin/env python3
"""Minimal havnai-like agent that processes jobs deterministically."""
from __future__ import annotations

import hashlib
import json
import os
import socket
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "jobs" / "inbox"
OUTBOX = ROOT / "jobs" / "outbox"
NODE_NAME = os.environ.get("HAVNAI_NODE", socket.gethostname())


def perform_work(payload: dict) -> dict:
    content = json.dumps(payload, sort_keys=True)
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    time.sleep(0.5)
    return {"payload_hash": digest, "size": len(content)}


def process_job(job_path: Path) -> None:
    raw = json.loads(job_path.read_text(encoding="utf-8"))
    job_id = raw.get("job_id", job_path.stem)
    tic = time.perf_counter()
    work = perform_work(raw.get("payload", {}))
    duration_ms = int((time.perf_counter() - tic) * 1000)
    record = {
        "job_id": job_id,
        "duration_ms": duration_ms,
        "node_name": NODE_NAME,
        "gpu_present": os.environ.get("GPU_PRESENT", "false").lower() == "true",
        "work": work,
    }
    output = OUTBOX / f"{job_id}.havnai.json"
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    job_path.unlink()
    print(f"completed {job_id} -> {output}")


def main() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    OUTBOX.mkdir(parents=True, exist_ok=True)
    print("havnai_mini_agent running. Ctrl+C to exit.")
    try:
        while True:
            for job_file in sorted(INBOX.glob("*.json")):
                process_job(job_file)
            time.sleep(1)
    except KeyboardInterrupt:
        print("agent stopped")


if __name__ == "__main__":
    main()
