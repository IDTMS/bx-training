#!/usr/bin/env python3
"""Collects quick triage data points into logs/triage.txt."""
from __future__ import annotations
import json
import os
import platform
import shutil
import socket
import subprocess
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "triage.txt"


def run_cmd(cmd: list[str]) -> str:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unavailable"


def collect() -> dict:
    uname = platform.uname()
    data = {
        "collected_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "kernel": uname.release,
        "python": sys.version.split()[0],
        "shell": os.environ.get("SHELL", "unknown"),
        "cwd": str(Path.cwd()),
        "path_sample": os.environ.get("PATH", "").split(os.pathsep)[:5],
        "disk_free": shutil.disk_usage(Path.cwd()).free,
        "process_sample": run_cmd(["ps", "-o", "pid,ppid,pcpu,pmem,command", "-p", str(os.getpid())]),
    }
    return data


def append_log(payload: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, sort_keys=True))
        fh.write("\n")


if __name__ == "__main__":
    append_log(collect())
    print(f"triage data appended to {LOG_PATH}")
