import express from 'express';
import config from './config.js';
import './db.js';
import webhookRoutes from './routes/webhooks.js';
import { startSessionCloseJob } from './jobs/sessionCloser.js';

const app = express();
app.use(express.json({ type: '*/*' }));

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.use('/webhooks', webhookRoutes);

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: 'Internal Server Error' });
});

app.listen(config.port, () => {
  console.log(`Food truck service listening on port ${config.port}`);
});

startSessionCloseJob();
