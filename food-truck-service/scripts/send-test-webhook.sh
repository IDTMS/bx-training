#!/usr/bin/env bash
set -euo pipefail

PAYLOAD_PATH=${1:-scripts/fake-payment.json}
SERVICE_URL=${SERVICE_URL:-http://localhost:4000/webhooks/square}

curl \
  -X POST \
  -H "Content-Type: application/json" \
  --data @"${PAYLOAD_PATH}" \
  "${SERVICE_URL}"
