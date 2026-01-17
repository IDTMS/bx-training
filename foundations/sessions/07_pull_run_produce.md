# Session 07 – Pull, Run, Produce

## Objective
Prove the workflow of pulling latest changes, running the agent, and producing a concrete output artifact from a demo job file.

## Why This Matters
- Demonstrates end-to-end readiness before layering GPU or network features.
- Reinforces the habit of producing artifacts on every run.
- Keeps local repos consistent across contributors.

## Prereqs
- Sessions 01–06 complete.
- `jobs/inbox/job-001.json` example file checked in.
- `.venv` active or Docker image built.

## Concepts
- Git pull discipline before running automation.
- Deterministic job definitions and outputs.
- Resetting state between runs.

## Steps
1. **Pull latest changes**
   ```bash
   git pull origin main
   ```
2. **Reset job folders**
   ```bash
   rm -f jobs/outbox/*
   cp jobs/inbox/job-001.json jobs/inbox/run-001.json
   ```
3. **Run the agent (local or Docker)**
   ```bash
   python projects/agent_basic/agent.py
   # or
   docker run --rm -it -v "$(pwd)/jobs/inbox:/jobs/inbox" -v "$(pwd)/jobs/outbox:/jobs/outbox" agent_basic:latest
   ```
4. **Observe output**
   ```bash
   ls jobs/outbox
   cat jobs/outbox/run-001.result.json
   ```
5. **Stop the agent** (`CTRL+C`).
6. **Document the run**
   ```bash
   echo "run-001 processed on $(date -u)" >> notes.md
   ```
7. **Reset command sequence (store for reuse)**
   ```bash
   cat <<'SH' > scripts/reset_jobs.sh
   #!/usr/bin/env bash
   set -euo pipefail
   rm -f jobs/inbox/*.json jobs/outbox/*.json
   cp jobs/inbox/job-001.json jobs/inbox/demo-run.json
   SH
   chmod +x scripts/reset_jobs.sh
   ```

## Deliverables
- Example job definition `jobs/inbox/job-001.json`.
- Result artifact `jobs/outbox/<run>.result.json` generated locally.
- Optional helper `scripts/reset_jobs.sh` for future runs.

## Done When
- [ ] `git pull` completes before execution.
- [ ] Agent run processes the copied job file without manual edits.
- [ ] Outbox contains a fresh `.result.json` file referencing the run ID.

## Troubleshooting
- **Agent processed original job file before copy:** recreate it with `cp jobs/inbox/job-001.json jobs/inbox/run-002.json` and rerun.
- **Reset script missing execute bit:** set via `chmod +x scripts/reset_jobs.sh`.
- **Docker job paths empty:** confirm you copied files before starting the container; container only sees current state at startup.
