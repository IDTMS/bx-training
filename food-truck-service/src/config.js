import dotenv from 'dotenv';

dotenv.config();

const requiredVars = ['DATABASE_URL', 'MERCHANT_ID'];
const missing = requiredVars.filter((name) => !process.env[name]);
if (missing.length) {
  throw new Error(`Missing required environment variables: ${missing.join(', ')}`);
}

const hours = (value) => value * 60 * 60 * 1000;

const config = {
  port: Number(process.env.PORT || 4000),
  databaseUrl: process.env.DATABASE_URL,
  merchantId: process.env.MERCHANT_ID,
  inactivityThresholdMs: hours(6),
  closeAfterMs: hours(1),
  cronExpression: '*/5 * * * *',
  twilio: {
    accountSid: process.env.TWILIO_ACCOUNT_SID,
    authToken: process.env.TWILIO_AUTH_TOKEN,
    fromNumber: process.env.TWILIO_FROM_NUMBER,
    adminNumber: process.env.ADMIN_PHONE_NUMBER,
    openingMessage: process.env.OPENING_SMS_BODY || 'Food truck session opened',
    closingMessage: process.env.CLOSING_SMS_BODY,
  },
};

export default config;
