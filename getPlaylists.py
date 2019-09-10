import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import paramiko
from paramiko import client
from paramiko.ssh_exception import SSHException
import redis
from redis import ConnectionError
import time

def ssh_command(ssh):
    # command = input("who")
    # ssh.invoke_shell()
    stdin_, stdout_, stderr_ = ssh.exec_command("redis-cli")
    stdout_.channel.recv_exit_status()
    print('Standard Error')
    print(stderr_.readlines)
    print('Standard OUT')
    print(stdout_.readline())
    ssh.close()


def ssh_connect():
    try:
        # client = paramiko.SSHClient()
        # print('Calling paramiko')
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.connect('206.72.203.244', username='dominik', password='Mangodog21')
        #
        #
        # chan = client.invoke_shell()
        # print('Log in Successful')
        # chan.send('redis-cli')
        # chan.send('\n')
        # time.sleep(5)
        # print('Command one sent')


        # chan.send('keys *')
        # chan.send('\n')
        # time.sleep(5)
        # resp = chan.recv(9999)
        # output = resp.decode('ascii').split(',')
        # print (''.join(output))


        # stdin_, stdout_, stderr_ = channel.exec_command("redis-cli")
        # print(str(stdout_.channel.recv_exit_status()))
        # print('Standard Error')
        # print(stderr_.readlines)
        # print('Standard OUT')
        # print(stdout_.readline())

        # chan.close()

        # chan.send('redis-cli')
        # chan.send('\n')
        # time.sleep(2)
        # print('Standard Error #2')
        # print('Standard OUT #2')
        # output = chan.recv(9999).decode('ascii').split(',')
        # print(''.join(output))
        # print('---------')
        # time.sleep(2)

        # channel.send('keys *\n')
        # channel.send('\n')
        # # channel.send('\n')
        # time.sleep(5)
        # # print(channel.recv(9999))
        # output = channel.recv(9999999999999).decode('ascii').split(',')
        # print(''.join(output))

        # pool = redis.ConnectionPool(host="localhost", port=6379, db=0, decode_responses=True)
        conn = redis.StrictRedis(host="127.0.0.1", port=6379, db=0, decode_responses=True)
        # print(conn)
        conn.ping()
        print('Connected!')
        print(conn.dbsize())

        # stdin_, stdout_, stderr_ = chan.exec_command("keys *")
        # # print(str(stdout_.channel.recv_exit_status()))
        # print('Standard Error')
        # print(stderr_.readlines())
        # print('Standard OUT')
        # print(stdout_.readlines())
        # chan.close()

        keys = conn.mget(conn.keys("*"))
        # chan.send(conn.mget(conn.keys("dominik*")))
        print(keys)
        print(conn.dbsize())
        # chan.close()
        # client.close()
        # chan.send('\n')
        # cursor =1
        # time.sleep(1)
        # for k in keys_s:
        #     chan.sendall('key_vals')
        # cursor, key = conn.sscan(cursor=cursor, count=1000000)
        # print(key)
        # time.sleep(10)
        # chan.send('\n')
        # time.sleep(1)
                # output_tmp = chan.recv(99999999).decode('ascii').split(',')
                # print('1111111')
                # print(output_tmp)
                # output = output_tmp.decode('utf-8').split(',')
                # print('2222222')
                # print(output)
                # out = output_tmp.decode('ascii').split(',')
                # print('33333333')
                # print(output)
                # # assert isinstance(resp, object)
                # print(''.join(output))
                # time.sleep(2)
                # chan.send('KEYS *')
                # chan.send('\n')
        # chan.send('\n')
        # time.sleep(2)
        # resp = chan.recv(9999).decode('ascii').split(',')
        # print(resp)
        # print(''.join(resp))

        conn.ping()
        print('Connected!')
        # keys = conn.keys('*')
        # chan.send('keys *')

        data = {}
        cursor = '0'
        for key in conn.keys('*'):
            cursor, key = conn.sscan(cursor=cursor, count=1000000)
            print(key)
            values = conn.mget(key)
            values = [value for value in values if not value == None]
            data.update(dict(zip(key, values)))
            # chan.send('\n')
        print(data)
        # conn.close()
        # redis_connect()
    except ConnectionError as ce:
        print('Connection #5 Failed')
        print(ce)
    except SSHException as sshe:
        print('Connection #3 Failed')
        # print(stdout_)
        # print(stderr_)
        print(sshe)
        # r = redis.StrictRedis(host='127.0.0.2', port=6379, db=0)
        # keys = r.keys()
        # print(keys)
        # chan.close()
        client.close()


    except paramiko.AuthenticationException:
        print("[-] Failed! ...")
    except Exception as e:
        print('Connection Failed # 4')
        print(e)

def redis_connect():
    try:
        # r = redis.StrictRedis('127.0.0.1', port=6379, db=0)
        r = redis.StrictRedis("127.0.0.2", port=6379, db=0)
        keys = r.keys()
        # print(keys)

    except ConnectionError as ce:
        print('Connection #2 Failed')
        print(ce)
    except Exception as e:
        print('Connection #3 Failed')
        print(e)
    print('Print KEYS')
    print(keys)

    r.close()






        # client_id = '5572530ac0664df2b34373f3f41db89b'
        # client_secret = '15734ca0cac44e3c8ee4cc238bc895cf'
        # uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:37i9dQZF1DXdgz8ZB7c2CP'
        # # uri = 'spotify:user:22okarqslvrgo5yvlkkfvr64a:playlist:2q1iIfQJgOkHumhCQg4Hrg'
        #
        # client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        #
        #
        # # if len(sys.argv) > 1:
        # #     user = sys.argv[1]
        #
        #
        #
        # username = uri.split(':')[2]
        # playlist_id = uri.split(':')[4]
        #
        # results = sp.user_playlist(username, playlist_id)
        # results = results['tracks']['items']
        # # print(results[0].keys())
        # playlist_art = {}
        # playlist_uri = {}
        # uri_list = list()
        # for track in results:
        #     art = list()
        #     for artist in track['track']['artists']:
        #         art.append(artist['name'])
        #     playlist_art.update({track['track']['name'] : art})
        #     playlist_uri.update({track['track']['name'] : track['track']['uri']})
        #     uri_list.append(track['track']['uri'])
        #     # print(track['track']['name'], art)


####################
# SSH Login
####################
# user = input("Username:")
user = "dominik"
# key = input("Public key full path:")
password = "Mangodog21"
# host = input("Target Hostname:")
host = "206.72.203.244"
# ssh_connect(host, user, key)
ssh_connect()


####################
# Redis Login
####################
# key_vals = redis_connect()
# print(key_vals)




# Audio analysis Doc
# https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/#rhythm
# analyze = sp.audio_analysis(playlist_uri['Loyal']) # dict_keys(['meta', 'track', 'bars', 'beats', 'tatums', 'sections', 'segments'])
# analyze = analyze['bars']
# print(analyze)
# print(analyze.keys())


# Audio Features
# https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
# analy = sp.audio_features(uri_list[0])
# print(analy)
