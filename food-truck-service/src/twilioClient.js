import twilio from 'twilio';
import config from './config.js';

let client = null;
if (
  config.twilio.accountSid &&
  config.twilio.authToken &&
  config.twilio.fromNumber &&
  config.twilio.adminNumber
) {
  client = twilio(config.twilio.accountSid, config.twilio.authToken);
}

export const sendSms = async (body) => {
  if (!client) {
    console.warn('Twilio is not configured; skipping SMS send.');
    return;
  }

  await client.messages.create({
    to: config.twilio.adminNumber,
    from: config.twilio.fromNumber,
    body,
  });
};

export default { sendSms };
