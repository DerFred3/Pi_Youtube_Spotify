import sqlite3
class QueueManager:
    dbPath = "queue.db"

    def __init__(self, dbpath :str, _sameThread=True):
        self.conn = sqlite3.connect(dbpath, check_same_thread=_sameThread)
        self.c = self.conn.cursor()
    
    def add(self, url:str, ctx:str):
        _url = '\'' + url + '\''
        _ctx = '\'' + ctx + '\''
        self.c.execute(f"INSERT INTO active_queue (id, url, ctx) VALUES (null, {_url}, {_ctx})")
        self.conn.commit()
    
    def addFirst(self, url:str, ctx:str):
        _url = '\'' + url + '\''
        _ctx = '\'' + ctx + '\''
        self.c.execute(f"INSERT INTO active_queue (id, url, ctx) VALUES (-1, {_url}, {_ctx})")
        self.conn.commit()

    def get(self):
        for row in self.c.execute("SELECT id, url, ctx FROM active_queue ORDER BY id ASC LIMIT 1"):
            _id = row[0]
            url = row[1]
            ctx = row[2]
            self.c.execute(f"DELETE FROM active_queue WHERE id = {_id}")
            self.c.execute(f"INSERT INTO log_queue (id, url, ctx) VALUES (null, '{url}', '{ctx}')")
            self.conn.commit()
            return {'url': str(url), 'ctx': str(ctx)}
    
    def resetQueue(self):
        # self.c.executescript()
        with open("initializeDb.sql") as f:
            content = f.read()
            self.c.executescript(content)
    
    def getQueueLength(self):
        for row in self.c.execute('SELECT COUNT(1) FROM active_queue'):
            return row[0]