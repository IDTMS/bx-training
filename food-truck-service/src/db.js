import pg from 'pg';
import config from './config.js';

const pool = new pg.Pool({
  connectionString: config.databaseUrl,
});

export const query = (text, params) => pool.query(text, params);

export const withTransaction = async (callback) => {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    const result = await callback(client);
    await client.query('COMMIT');
    return result;
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
};

export default {
  query,
  withTransaction,
};
