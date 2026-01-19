# Food Truck Auto-Announcer

Minimal Node.js (Express) backend that listens for Square `payment.created` webhooks, tracks food truck sessions, and sends SMS alerts through Twilio. Designed for a single merchant with no frontend or auth.

## Features
- Receives Square `payment.created` events via `/webhooks/square`.
- Treats the first payment after 6 hours of inactivity as the start of a new Session record.
- Updates `last_sale_at` for every payment and stores Session lifecycle timestamps in Postgres.
- Runs a 5-minute cron job that closes Sessions after 60 minutes without sales and can emit an optional closing SMS.
- Sends Twilio SMS alerts when sessions open (and optionally when they close).
- Includes a `Spot` table that can be seeded for future location logic.

## Requirements
- Node.js 18+
- PostgreSQL 14+
- `ngrok` (for exposing the webhook endpoint)

## Configuration
Copy the sample environment file and update the values:

```bash
cp .env.example .env
```

Required variables:

- `DATABASE_URL` – Postgres connection string.
- `MERCHANT_ID` – Square merchant ID this service accepts events for.
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER`, `ADMIN_PHONE_NUMBER` – Twilio credentials + destination phone. SMS sending is skipped automatically when any of these are missing.
- `OPENING_SMS_BODY` – Message sent when a session opens (defaults to `Food truck session opened`).
- `CLOSING_SMS_BODY` – Optional closing message. Leave blank to disable.

## Database setup
1. Create a database (example uses `food_truck`).
2. Enable UUID helpers and run the schema + seed scripts:

```bash
psql $DATABASE_URL <<'SQL'
CREATE EXTENSION IF NOT EXISTS pgcrypto;
\i sql/schema.sql
\i sql/seed_spots.sql
SQL
```

## Running locally
Install dependencies and start the server:

```bash
npm install
npm run start
```

The service listens on `PORT` (default `4000`). Health check lives at `GET /health`.

## Exposing the webhook with ngrok
In a second terminal, expose the local port:

```bash
ngrok http 4000
```

Copy the generated HTTPS URL and register `https://<random>.ngrok.io/webhooks/square` with Square's webhook configuration.

## Testing with fake payloads
You can replay sample payloads without Square:

```bash
# ensure the server is running
./scripts/send-test-webhook.sh
```

Override the payload path or remote URL if needed:

```bash
SERVICE_URL=https://<ngrok host>/webhooks/square \
  ./scripts/send-test-webhook.sh /path/to/custom-payload.json
```

Update the `merchant_id` within `scripts/fake-payment.json` (and `data.object.payment.merchant_id`) so it matches your configured `MERCHANT_ID`.

## How it works
- **Webhook ingestion** (`src/routes/webhooks.js`): accepts JSON and filters for `payment.created` events.
- **Session service** (`src/services/sessionService.js`): stores/updates sessions in Postgres, enforces the 6-hour inactivity requirement for opening, and updates `last_sale_at` on every payment.
- **Scheduler** (`src/jobs/sessionCloser.js`): runs every 5 minutes and closes the active session when `last_sale_at` is >60 minutes ago. When closed, an optional SMS is sent.
- **Twilio integration** (`src/twilioClient.js`): uses environment variables for credentials and safely no-ops when creds are missing.

This repository intentionally omits any frontend, ads, AI, social media APIs, or payment processing logic—only the Square webhook listener, Postgres persistence, and Twilio notifications are included.
