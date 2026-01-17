# syscheck

Minimal command-line utility to snapshot local system metadata as JSON. Intended for quick validation during Session 3 and later automation tasks.

## Usage
```bash
python projects/syscheck/syscheck.py --pretty
python projects/syscheck/syscheck.py --output projects/syscheck/examples/output.json --pretty
```
Use `--log-level DEBUG` if you need trace information while debugging.
