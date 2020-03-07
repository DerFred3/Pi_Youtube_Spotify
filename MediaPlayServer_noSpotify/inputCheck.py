#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
#import spotipy.util as util
import re
import flags

#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="005924e55fb146958722d9431728c17b",client_secret="fb76aa759c3d46c2b5df2a515d669412"))

## Prüfen, ob die Interpret-Song-Kombination existiert
#def checkSong(artistName, songName):
#    results = spotify.search(q='artist:' + artistName + ' track:' + songName, type='track', limit=1)
#    items = results['tracks']['items']
#
#    if len(items) > 0:
#        return items[0]
#    else:
#        return None
#
# Prüfen, ob der Link ein YouTube oder Spotify Link ist
def checkSpotifyYoutube(link):
    # Zeit für Regex
    regex_spotify = '^(spotify:track:[\w]+([\n]*))$' # Spotify-URI
    regex_youtube = '^https:\/\/((www.youtube.com\/watch\?v=[\w+-]+)|(youtu.be\/[\w+-]+))$' # Youtube-Link oder Youtu.be-Link
    
    match = re.search(regex_spotify, link)
    if match:
        return flags.ctx_spotify
    else:
        match = re.search(regex_youtube, link)
        if match:
            return flags.ctx_youtube
    
    return None