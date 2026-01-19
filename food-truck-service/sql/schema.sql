CREATE TABLE IF NOT EXISTS sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status TEXT NOT NULL CHECK (status IN ('ACTIVE', 'CLOSED')),
    started_at TIMESTAMPTZ NOT NULL,
    last_sale_at TIMESTAMPTZ,
    closed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS spots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    lat NUMERIC(9,6) NOT NULL,
    lon NUMERIC(9,6) NOT NULL,
    radius INTEGER NOT NULL DEFAULT 250
);
