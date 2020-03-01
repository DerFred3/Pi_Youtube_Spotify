import sqlite3, vlc, pafy, time, queueManager, flags
class PlayerManager:
    
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_fullscreen(True)
        self.qManager = queueManager.QueueManager(queueManager.QueueManager.dbPath, _sameThread=False)

        
    def start(self):
        while True:
            url = self.qManager.get()
            if url:
                self.play(url)
            else:
                if self.player.is_playing():
                    self.player.pause()
                else:
                    time.sleep(1)


    def play(self, url :str):
        try:
            besturl = pafy.new(url).getbest().url
            # besturl = pafy.new(url).getbestaudio().url
            media = self.instance.media_new(besturl)
            self.player.set_media(media)
            self.player.play()
            time.sleep(1.5)
            # time.sleep(self.player.get_length() / 1000)
            while self.player.is_playing():
                if flags.doPause:
                    self.player.pause()
                    while flags.doPause:
                        time.sleep(0.1)
                    self.player.pause()

                if flags.doSkip:
                    flags.setSkip(False)
                    break
                else:
                    time.sleep(0.1)
        except:
            return