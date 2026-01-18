# Session 0: Environment Gate

## Why Session 0 Exists
Session 0 verifies that your local workstation can work with this repository. Before touching infrastructure or automation topics, you must prove you can clone code, create isolated Python environments, and run verification scripts without guesswork. This gate keeps later labs realistic and prevents chasing tooling issues mid-way through an exercise.

## Requirements
- GitHub account with SSH or HTTPS access configured.
- Git installed with PATH access (`git --version` works).
- Python 3.10+ with the `venv` module.
- Terminal access on macOS, Linux, or Windows via WSL.
- Basic familiarity with copying commands and reading terminal output.

## Step-by-Step Setup
1. **Confirm GitHub connectivity**
   ```bash
   git --version
   ssh -T git@github.com   # optional but recommended if using SSH
   ```
   Resolve authentication prompts before proceeding.

2. **Clone this repository**
   ```bash
   cd ~/workdir   # replace with your preferred projects folder
   git clone https://github.com/IDTMS/bx-training.git
   cd foundations
   ```
   Use the HTTPS URL if SSH is not configured.

3. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv            # use `python -m venv .venv` on Windows if python3 is unavailable
   source .venv/bin/activate        # macOS/Linux/WSL
   .venv\Scripts\activate           # Windows PowerShell / cmd
   ```
   The prompt should show `(.venv)` when the environment is active.

4. **Install minimal dependencies (if any)**
   ```bash
   python -m pip install --upgrade pip
   ```
   Later sessions will add `requirements.txt` or tooling-specific installs.

5. **Run the verification script**
   ```bash
   python scripts/hello.py
   ```
   Expect a simple success message. If the script file does not exist yet, create it with:
   ```bash
   mkdir -p scripts
   cat <<'PY' > scripts/hello.py
   print("session 0: environment online")
   PY
   ```

6. **Deactivate when finished**
   ```bash
   deactivate
   ```

## Common Issues / Notes
- **Permission errors:** Ensure the target folder is writable; avoid spaces in folder names when possible.
- **Missing `venv`:** Install the Python `venv` package (`sudo apt install python3-venv` on Ubuntu/Debian) and rerun the environment creation step.
- **`python3` not found:** Use `python` instead, but confirm it points to Python 3.10+ (`python --version`).
- **SSL or auth failures:** Double-check your GitHub SSH keys or HTTPS credentials; run `ssh -v git@github.com` for diagnostics.
- **Stale environments:** Remove `.venv` (`rm -rf .venv` or `rmdir /s .venv`), then recreate if dependencies become inconsistent.
- Session 0 is mandatory. Do not start later sessions until you can complete every step reproducibly.
