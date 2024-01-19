import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
cid = 'd7f0502e866d4206954039335d54a638'
secret = '2f10f5a7e02949009166e5295e1c679d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)


birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])