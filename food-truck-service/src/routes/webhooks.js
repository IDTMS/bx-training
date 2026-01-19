import express from 'express';
import { handlePaymentCreated } from '../services/sessionService.js';

const router = express.Router();

router.post('/square', async (req, res, next) => {
  try {
    const eventType = req.body?.type || req.body?.event_type;
    if (eventType !== 'payment.created') {
      return res.status(202).json({ status: 'ignored' });
    }

    await handlePaymentCreated(req.body);
    return res.status(202).json({ status: 'received' });
  } catch (error) {
    return next(error);
  }
});

export default router;
