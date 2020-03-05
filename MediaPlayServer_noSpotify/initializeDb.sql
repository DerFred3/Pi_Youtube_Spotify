INSERT INTO log_queue
SELECT null, url, ctx FROM active_queue;

DELETE FROM active_queue;

UPDATE sqlite_sequence
   SET seq = 1
 WHERE name = 'active_queue';