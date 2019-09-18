import spotipy
import redis
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '5572530ac0664df2b34373f3f41db89b'
client_secret = '15734ca0cac44e3c8ee4cc238bc895cf'
uri_playL_list = ['spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:37i9dQZF1DXdgz8ZB7c2CP', 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:6tJ0eB80eKJtFDvK3pJ7H3',
                  'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:17resVfiqMumDlv5Ffmts6', 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:4WRdMMQSDWPqkBlrt7iERG']
# uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:2q1iIfQJgOkHumhCQg4Hrg'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



username = uri_playL_list[0].split(':')[2]

playlist_art = {}
playlist_uri = {}
playid = 5

track_uri_list = list()
playlist_uri_list = list()
for uri in uri_playL_list:
    playlist_uri_list.append(uri)
    results = sp.user_playlist(username, uri)
    results = results['tracks']['items']
    for track in results:
        track_uri_list.append(track['track']['uri'])

r = redis.Redis(host='localhost', port=6379)
r.flushdb()
pipe = r.pipeline()
for play_val in playlist_uri_list:
    # for track_val in track_uri_list:
    pipe.hset(username, play_val, str(track_uri_list))
pipe.execute()

print(r.hkeys(username))
print(r.dbsize())
print(r.hkeys('22okarqslvrgo5yvlkkfvr64a'))
print(r.dbsize())
