import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# user = '22okarqslvrgo5yvlkkfvr64a?'

# if len(sys.argv) > 1:
#     user = sys.argv[1]

uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:2q1iIfQJgOkHumhCQg4Hrg'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)
# print(results['tracks']['items'])
for track in results['tracks']['items']:
    art = list()
    for artist in track['track']['artists']:
        art.append(artist['name'])
    print(track['track']['name'] + '   ***   ' + str(art))
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
