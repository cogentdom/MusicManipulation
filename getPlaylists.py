import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = '5572530ac0664df2b34373f3f41db89b'
client_secret = '15734ca0cac44e3c8ee4cc238bc895cf'
uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:2q1iIfQJgOkHumhCQg4Hrg'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# if len(sys.argv) > 1:
#     user = sys.argv[1]



username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)
results = results['tracks']['items']
# print(results[0].keys())
playlist = {}
for track in results:
    art = list()
    for artist in track['track']['artists']:
        art.append(artist['name'])
    playlist.update({track['track']['name'] : art})
print(playlist)


# trackz = results['tracks']['items'][0]['track']
# print (results['tracks'])
# for track in results['tracks']['items'][0]['track']:
#     print('\n********\n' + track.get('name'))


# playlists = sp.user_playlists(user)
#
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
