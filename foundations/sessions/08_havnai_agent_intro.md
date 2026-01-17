# Session 08 – HavnAI Agent Intro

## Objective
Implement a minimal HavnAI-style agent that consumes JSON jobs, performs deterministic work, and writes structured results containing metadata such as duration, node name, and GPU presence.

## Why This Matters
- HavnAI agents are just disciplined long-running processes with auditable outputs.
- Metadata-rich results allow schedulers and operators to reason about performance.
- Determinism enables reproducible verification before any distributed coordination exists.

## Prereqs
- Sessions 01–07 complete.
- `.venv` active.
- `projects/havnai_mini_agent/` available.

## Concepts
- Reading/writing JSON job payloads.
- Hashing payload data to simulate deterministic work.
- Capturing runtime metrics (duration, node info, GPU flag).

## Steps
1. **Review the project files**
   ```bash
   tree projects/havnai_mini_agent
   sed -n '1,160p' projects/havnai_mini_agent/agent.py
   ```
2. **Prepare environment variables**
   ```bash
   export HAVNAI_NODE=$(hostname -s)
   export GPU_PRESENT=false
   ```
3. **Start the agent**
   ```bash
   python projects/havnai_mini_agent/agent.py
   ```
4. **Submit a job**
   ```bash
   cat <<'JSON' > jobs/inbox/havnai-demo.json
   {
     "job_id": "havnai-demo",
     "payload": {
       "task": "hash",
       "data": "hello foundations"
     }
   }
   JSON
   ```
5. **Inspect the output**
   ```bash
   cat jobs/outbox/havnai-demo.havnai.json
   ```
6. **Stop the agent** (`CTRL+C`).
7. **Document capabilities in README**
   ```bash
   less projects/havnai_mini_agent/README.md
   ```

## Deliverables
- `projects/havnai_mini_agent/agent.py` implementing the workflow.
- `projects/havnai_mini_agent/README.md` explaining environment vars and usage.
- Output artifacts `jobs/outbox/<job>.havnai.json` from a real run.

## Done When
- [ ] Agent runs continuously and processes at least one job.
- [ ] Output JSON includes `job_id`, `duration_ms`, `node_name`, and `gpu_present`.
- [ ] README clearly states how to set optional environment variables.

## Troubleshooting
- **`json.decoder.JSONDecodeError`:** ensure job files contain valid JSON and UTF-8 encoding.
- **`Permission denied` deleting jobs:** stop the agent before manually editing files; it removes processed jobs automatically.
- **Node name missing:** set `HAVNAI_NODE` explicitly if `os.uname` is unavailable (older Windows hosts—use WSL instead).
