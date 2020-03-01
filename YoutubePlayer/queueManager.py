import sqlite3
class QueueManager:
    dbPath = "YoutubePlayer/queue.db"

    def __init__(self, dbpath :str, _sameThread=True):
        self.conn = sqlite3.connect(dbpath, check_same_thread=_sameThread)
        self.c = self.conn.cursor()
    
    def add(self, url :str):
        _url = '\'' + url + '\''
        self.c.execute(f"INSERT INTO active_queue (id, url) VALUES (null, {_url})")
        self.conn.commit()
    
    def get(self):
        for row in self.c.execute("SELECT id, url FROM active_queue ORDER BY id ASC LIMIT 1"):
            _id = row[0]
            url = row[1]
            self.c.execute(f"DELETE FROM active_queue WHERE id = {_id}")
            self.c.execute(f"INSERT INTO log_queue (id, url) VALUES (null, '{url}')")
            self.conn.commit()
            return url
    
    def resetQueue(self):
        # self.c.executescript()
        with open("YoutubePlayer/initializeDb.sql") as f:
            content = f.read()
            self.c.executescript(content)