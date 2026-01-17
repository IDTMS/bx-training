# Session 02 – Shell & Processes

## Objective
Practice manipulating paths, permissions, and processes while building a reusable triage script that captures local system data.

## Why This Matters
- Quickly answering "what changed" depends on disciplined shell usage.
- Fast triage reduces time spent guessing about environment drift.
- Logs created here become evidence for later sessions.

## Prereqs
- Session 01 complete.
- `.venv` active.
- `logs/` directory writeable (created automatically).

## Concepts
- PATH inspection, environment variables, piping output to files.
- Process basics: listing, filtering, and capturing information for support.

## Steps
1. **Inspect shell context**
   ```bash
   pwd
   echo "$SHELL"
   echo "$PATH" | tr ':' '\n' | head
   ```
2. **Review permissions**
   ```bash
   ls -l scripts
   chmod +x scripts/*.py
   ```
3. **Create/verify the triage script**
   ```bash
   python scripts/triage_collect.py
   tail logs/triage.txt
   ```
   Each run appends JSON to `logs/triage.txt`.
4. **Explore processes**
   ```bash
   ps -ef | head
   ps -p $$ -o pid,ppid,command
   ```
5. **Demonstrate piping/logging**
   ```bash
   env | sort | head > logs/env_head.txt
   ```
6. **Record shell snapshot (optional)**
   ```bash
   date -u >> logs/shell_sessions.log
   ```

## Deliverables
- `scripts/triage_collect.py` (provided) executed and confirmed.
- Updated `logs/triage.txt` containing the newest JSON line.

## Done When
- [ ] `logs/triage.txt` shows a fresh entry for this session.
- [ ] Permissions on `scripts/triage_collect.py` allow execution.
- [ ] You can identify a running process via `ps` output.

## Troubleshooting
- **`ps` restricted on macOS:** preface with `sudo` if needed, or use `ps aux` for broader output.
- **No `logs` directory:** create it manually (`mkdir -p logs`).
- **Unicode errors when piping env vars:** ensure locale is UTF-8 (`export LC_ALL=en_US.UTF-8`).
