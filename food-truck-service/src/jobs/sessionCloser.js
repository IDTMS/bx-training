import cron from 'node-cron';
import config from '../config.js';
import { closeInactiveSession } from '../services/sessionService.js';

export const startSessionCloseJob = () => {
  cron.schedule(config.cronExpression, async () => {
    try {
      const closed = await closeInactiveSession();
      if (closed) {
        console.log('Session closed due to inactivity', closed.id);
      }
    } catch (error) {
      console.error('Failed to close inactive session', error);
    }
  });
};
