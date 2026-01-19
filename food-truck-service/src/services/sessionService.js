import config from '../config.js';
import { withTransaction } from '../db.js';
import twilio from '../twilioClient.js';

const ACTIVE_STATUS = 'ACTIVE';
const CLOSED_STATUS = 'CLOSED';

const selectActiveSession = async (client) => {
  const { rows } = await client.query(
    `SELECT * FROM sessions WHERE status = $1 ORDER BY started_at DESC LIMIT 1`,
    [ACTIVE_STATUS]
  );
  return rows[0] || null;
};

const selectLatestSession = async (client) => {
  const { rows } = await client.query(
    `SELECT * FROM sessions ORDER BY last_sale_at DESC NULLS LAST LIMIT 1`
  );
  return rows[0] || null;
};

const insertSession = async (client, timestamp) => {
  const { rows } = await client.query(
    `INSERT INTO sessions (status, started_at, last_sale_at)
     VALUES ($1, $2, $2)
     RETURNING *`,
    [ACTIVE_STATUS, timestamp.toISOString()]
  );
  return rows[0];
};

const touchSession = async (client, sessionId, timestamp) => {
  await client.query(`UPDATE sessions SET last_sale_at = $1 WHERE id = $2`, [
    timestamp.toISOString(),
    sessionId,
  ]);
};

const closeSessionById = async (client, sessionId, closedAt) => {
  const { rows } = await client.query(
    `UPDATE sessions
     SET status = $1,
         closed_at = $2
     WHERE id = $3
     RETURNING *`,
    [CLOSED_STATUS, closedAt.toISOString(), sessionId]
  );
  return rows[0] || null;
};

const maybeSendOpeningSms = async () => {
  if (!config.twilio.openingMessage) {
    return;
  }
  await twilio.sendSms(config.twilio.openingMessage);
};

const maybeSendClosingSms = async () => {
  if (!config.twilio.closingMessage) {
    return;
  }
  await twilio.sendSms(config.twilio.closingMessage);
};

export const handlePaymentCreated = async (payload) => {
  const merchantId =
    payload?.data?.object?.payment?.merchant_id || payload?.merchant_id;

  if (merchantId && merchantId !== config.merchantId) {
    console.log('Ignoring webhook for merchant', merchantId);
    return;
  }

  const createdAt =
    payload?.data?.object?.payment?.created_at || new Date().toISOString();
  const paymentTime = new Date(createdAt);

  await withTransaction(async (client) => {
    let activeSession = await selectActiveSession(client);
    let sessionToUpdate = activeSession;

    if (!activeSession) {
      const latestSession = await selectLatestSession(client);
      const lastSale = latestSession?.last_sale_at
        ? new Date(latestSession.last_sale_at)
        : null;
      const inactiveForMs = lastSale ? paymentTime - lastSale : Infinity;
      const qualifiesForOpeningSms =
        inactiveForMs >= config.inactivityThresholdMs;

      sessionToUpdate = await insertSession(client, paymentTime);
      if (qualifiesForOpeningSms) {
        await maybeSendOpeningSms();
      }
    }

    await touchSession(client, sessionToUpdate.id, paymentTime);
  });
};

export const closeInactiveSession = async () => {
  return withTransaction(async (client) => {
    const activeSession = await selectActiveSession(client);
    if (!activeSession || !activeSession.last_sale_at) {
      return null;
    }

    const lastSale = new Date(activeSession.last_sale_at);
    const elapsedMs = Date.now() - lastSale.getTime();
    if (elapsedMs < config.closeAfterMs) {
      return null;
    }

    const closed = await closeSessionById(client, activeSession.id, new Date());
    await maybeSendClosingSms();
    return closed;
  });
};
