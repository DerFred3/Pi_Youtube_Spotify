import pyautogui as gui
import time

# position spoitfy search bar in fullscreen mode [427,77]
# position spotify play song after search [401,291]


# Um die Funktion zu nutzen, muss klar sein, dass der Songname eindeutig ist
# hierfür ist eine Validierung über die Spotify Web-API vonnöten
# dort kann mit einem beliebigen String gesucht werden, danach der eindeutige "Interpret Titel" an die Funktion weitergegeben
def playSong(songName:str):
    # Maus auf die Suchzeile, klicken und Songname eintippen
    gui.moveTo(427,77,duration=1)
    gui.click(clicks=3)
    time.sleep(0.75)
    gui.write(songName)
    time.sleep(1)

    # Ersten Eintrag auswählen und abspielen
    gui.moveTo(401,291, duration=1)
    gui.click()