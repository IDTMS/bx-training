#!/usr/bin/env bash
set -euo pipefail
rm -f jobs/inbox/*.json 2>/dev/null || true
rm -f jobs/outbox/*.json 2>/dev/null || true
cp jobs/inbox/job-001.json jobs/inbox/demo-run.json
