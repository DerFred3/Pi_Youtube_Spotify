import sqlite3, vlc, pafy, time, queueManager, flags#, spotifyManager
class PlayerManager:
    
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_fullscreen(True)
        self.qManager = queueManager.QueueManager(queueManager.QueueManager.dbPath, _sameThread=False)
        self.yt_help_counter = 0 # Beim aufrufen des ersten Videos darf der Kontext nicht geändert werden per ALT+TAB

    def start(self):
        while True:
            qReturn = self.qManager.get()
            if qReturn:
                url = qReturn['url']
                ctx = qReturn['ctx']
                
                if ctx == flags.ctx_youtube:
                    if url:
                        self.playYoutube(url)
                    else:
                        if self.player.is_playing():
                            self.player.pause()
                        else:
                            time.sleep(1)
                elif ctx == flags.ctx_spotify:
                    self.playSpotify(url)

    #def playSpotify(self, url:str):
    #    try:
    #        duration = spotifyManager.getDuration(url)
    #        spotifyManager.playSong(url)
    #        elapsedTime = 0
    #        while True:
    #            if flags.doPause:
    #                spotifyManager.playPause()
    #                while flags.doPause:
    #                    time.sleep(0.1)
    #                spotifyManager.playPause()
    #            
    #            if flags.doSkip:
    #                flags.setSkip(False)
    #                break                
    #
    #            time.sleep(1)
    #            elapsedTime += 1
    #            if elapsedTime >= duration:
    #                break
    #        
    #        spotifyManager.playPause() # Pausieren, damit nicht das nächste Spotify Lied abgespielt wird
    #    except:
    #        return
    
    def playYoutube(self, url:str):
        try:
            besturl = pafy.new(url).getbest().url
            # besturl = pafy.new(url).getbestaudio().url
            media = self.instance.media_new(besturl)
            self.player.set_media(media)

            #if flags.appCtx != flags.ctx_youtube and self.yt_help_counter > 0:
            #    spotifyManager.changeCtx(flags.ctx_youtube)
            #elif flags.appCtx != flags.ctx_youtube and self.yt_help_counter == 0:
            #    self.yt_help_counter = 1
            #    flags.setContext(flags.ctx_youtube)
            
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
                    self.player.pause()
                    break
                else:
                    time.sleep(0.1)
        except:
            return