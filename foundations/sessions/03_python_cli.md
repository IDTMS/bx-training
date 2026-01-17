# Session 03 – Python CLI

## Objective
Build a minimal CLI using `argparse` and `logging` that emits JSON describing the host, then capture an example output file.

## Why This Matters
- Every automation effort needs a predictable entry point.
- Structured output (JSON) enables chaining tools later.
- Logging now prevents silent failures when sessions grow.

## Prereqs
- Sessions 01–02 complete.
- `.venv` active with Python 3.10+.
- `projects/syscheck/` folder available.

## Concepts
- `argparse` for CLI arguments.
- Python logging basics.
- JSON serialization and file output.

## Steps
1. **Review the project layout**
   ```bash
   tree projects/syscheck || ls -R projects/syscheck
   ```
2. **Inspect the CLI**
   ```bash
   python projects/syscheck/syscheck.py --help
   ```
3. **Run with stdout output**
   ```bash
   python projects/syscheck/syscheck.py --pretty
   ```
4. **Write to disk**
   ```bash
   python projects/syscheck/syscheck.py \
     --output projects/syscheck/examples/output.json \
     --pretty
   ```
5. **Enable debug logging**
   ```bash
   python projects/syscheck/syscheck.py --log-level DEBUG
   ```
6. **Review README for context**
   ```bash
   less projects/syscheck/README.md
   ```

## Deliverables
- `projects/syscheck/syscheck.py` (committed).
- `projects/syscheck/README.md` with usage instructions.
- Sample JSON payload at `projects/syscheck/examples/output.json`.

## Done When
- [ ] CLI help output displays usage and arguments.
- [ ] JSON file exists under `projects/syscheck/examples/`.
- [ ] Logging statements appear when `--log-level DEBUG` is set.

## Troubleshooting
- **`Permission denied` on script:** set execute bit or call via `python path/to/syscheck.py`.
- **Invalid path for `--output`:** ensure parent directory exists (`mkdir -p projects/syscheck/examples`).
- **`ModuleNotFoundError`:** run commands from repo root with `.venv` active to avoid import issues.
