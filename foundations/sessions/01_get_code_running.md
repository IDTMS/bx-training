# Session 01 – Get Code Running

## Objective
Clone the repository, read the instructions, activate the Python environment, and successfully run the provided scripts.

## Why This Matters
- Establishes a reproducible workflow for pulling and executing repo content.
- Confirms shell, Git, and Python tooling work the same way as the rest of the course.

## Prereqs
- Session 0 completed on macOS/Linux or Windows via WSL.
- Python 3.10+ with `venv` already created (`.venv`).
- GitHub access to this repository.

## Concepts
- Git clone, pull, and status.
- Activating `venv` and running Python scripts from repo root.

## Steps
1. **Sync the repository**
   ```bash
   cd ~/projects/foundations                 # or your workspace
   git pull origin main                      # run `git clone` first time
   ```
2. **Read the onboarding files**
   ```bash
   less README.md
   less SESSION_0.md
   ```
   Take short notes in `notes.md` if helpful (optional artifact).
3. **Activate Python environment**
   ```bash
   source .venv/bin/activate                 # macOS/Linux/WSL
   # Windows (WSL preferred): same as above
   ```
4. **Run baseline scripts**
   ```bash
   python scripts/triage_collect.py
   python scripts/gpu_check.py || true       # prints JSON; continue even if torch missing
   ```
   Confirm the console output matches expectations.
5. **Capture observations** (optional)
   ```bash
   echo "Session 01 run on $(date -u)" >> notes.md
   ```

## Deliverables
- Optional `notes.md` or run log documenting the commands you executed.

## Done When
- [ ] `git pull` completes without conflict.
- [ ] `.venv` is active and Python scripts run without stack traces.
- [ ] `logs/triage.txt` contains a new entry from today.

## Troubleshooting
- **`git pull` errors:** run `git status` and stash/commit local work before pulling.
- **`python` points to 2.x:** invoke `python3` explicitly or update shell aliases.
- **Permission errors on scripts:** ensure execute bit is set (`chmod +x scripts/*.py`) or invoke via `python <path>`.
