import pyautogui as gui
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time, math, flags

def getDuration(songURI):
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='005924e55fb146958722d9431728c17b', client_secret='fb76aa759c3d46c2b5df2a515d669412'))

    results = spotify.track(songURI)

    return math.ceil(results['duration_ms']/1000)

# Nachdem das Lied zu Ende ist, muss Pause gedrückt werden, weil sonst bei der Vorbereitung 
# der nächsten Position der Queue der nächste Song in Spotify abgespielt wird
# --> Ist außerdem sauberer das Lied mit einer Pause zu beenden


# Es wird nicht der Interpret in Kombination mit Songname, sondern die Song URI übergeben
# Fokus muss bereits auf Spotify sein
# Sucht den Song und spielt diesen ab
def playSong(songURI):
    checkCtx() # Kontext prüfen und ggf. ändern

    # Shortcut für die Suchzeile, Song-URI eintippen und per doppelt ENTER den Song abspielen
    gui.hotkey('ctrl', 'l') # Fokus auf die Suchzeile
    time.sleep(0.5)
    gui.write(songURI)
    gui.press('enter')
    time.sleep(0.5)
    gui.press('enter')
    gui.press('enter')

    # Sleep und Pause muss in der aufrufenden Funktion gehandelt werden, falls manuell pausiert wird
    #time.sleep(duration)
    #gui.press('space') #playpause wollte nicht, dann muss die Spacebar dafür hinhalten

def playPause():
    checkCtx() # Kontext prüfen und ggf. ändern
    gui.press('space')

def checkCtx():
    if flags.appCtx != flags.ctx_spotify:
        changeCtx(flags.ctx_spotify)

def changeCtx(_ctx):
    gui.keyDown('alt')
    time.sleep(0.5)
    gui.keyDown('tab')
    time.sleep(0.1)
    gui.keyUp('tab')
    time.sleep(0.5)
    gui.keyUp('alt')
    flags.setContext(_ctx)
    time.sleep(2) # Zwei Sekunden Delay, damit der Kontext sauber gewechselt werden kann