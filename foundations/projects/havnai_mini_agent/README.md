# havnai_mini_agent

Reference implementation for Session 8. The agent watches `jobs/inbox` for JSON job files, runs a deterministic placeholder workload, and emits structured results to `jobs/outbox`.

## Run
```bash
source .venv/bin/activate
python projects/havnai_mini_agent/agent.py
```
Set `HAVNAI_NODE` to override the node name, and optionally `GPU_PRESENT=true` if your workstation exposes a GPU.
