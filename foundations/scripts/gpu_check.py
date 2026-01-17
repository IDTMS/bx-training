#!/usr/bin/env python3
"""Report host GPU awareness without requiring heavy dependencies."""
from __future__ import annotations

import json
import platform
import sys


def detect_cuda() -> dict:
    try:
        import torch  # type: ignore
    except ModuleNotFoundError:
        return {
            "torch_installed": False,
            "cuda_available": False,
            "notes": "Install torch with CUDA support if GPU work is required."
        }
    return {
        "torch_installed": True,
        "cuda_available": bool(torch.cuda.is_available()),
        "notes": "Enable CUDA toolkit and drivers if availability is False.",
    }


def main() -> None:
    payload = {
        "os": platform.platform(),
        "python_version": sys.version.split()[0],
        "gpu": detect_cuda(),
    }
    print(json.dumps(payload, indent=2))
    if not payload["gpu"]["torch_installed"]:
        print("torch not installed; install via pip or conda when GPU testing is needed.")


if __name__ == "__main__":
    main()
