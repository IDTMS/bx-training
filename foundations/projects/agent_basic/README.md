# agent_basic

A minimal long-running agent that watches `jobs/inbox` and writes processed JSON artifacts to `jobs/outbox`.

## Run locally
```bash
source .venv/bin/activate
python projects/agent_basic/agent.py
```
Drop files into `jobs/inbox/` (JSON or text). The agent removes each file after converting it to `jobs/outbox/<name>.result.json`.

## Docker usage (after Session 6)
```bash
cd projects/agent_basic
docker build -t agent_basic:latest .
docker run --rm \
  -v "$(pwd)/../../jobs/inbox:/jobs/inbox" \
  -v "$(pwd)/../../jobs/outbox:/jobs/outbox" \
  agent_basic:latest
```
Use `CTRL+C` to stop the container; output artifacts remain on the host.
