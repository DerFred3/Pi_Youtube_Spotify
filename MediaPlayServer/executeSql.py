import sqlite3

dbPath = "queue.db"

conn = sqlite3.connect(dbPath, check_same_thread=True)
c = conn.cursor()

#c.execute(f'ALTER TABLE active_queue ADD ctx VARCHAR2(100)')
#c.execute(f'ALTER TABLE log_queue ADD ctx VARCHAR2(100)')

#for row in c.execute("SELECT id, url, ctx FROM log_queue ORDER BY id desc LIMIT 1"):
#    _id = row[0]
#    url = row[1]
#    ctx = row[2]
#
#    print(_id)
#    print(url)
#    print(ctx)

#c.execute('DELETE FROM log_queue')