import paramiko
from paramiko import transport
import socket
import redis

def sock_bind():
    s = socket.socket()
    s.bind(('localhost', 6379))

    s.listen(1)
    c, addr = s.accept()
    return c, addr

client = paramiko.SSHClient()
print('Calling paramiko')
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('206.72.203.244', username='dominik', password='Mangodog21')
#
remote_conn = client.invoke_shell()
# remote_conn.send('redis-cli\n')

s = socket.socket()
s.connect(('localhost', 6379))

transport = transport.Transport(s)
# transport.connect(username='dominik', password='Mangodog21')

conn = client.get_transport().open_session()
resp = remote_conn.recv(1024).decode('ascii').split(',')
print(''.join(resp))

r = redis.StrictRedis(host='127.0.0.1', port=6379,  db=0)
# keys = r.keys('*dom')
print(r.dbsize())
remote_conn.send(r.keys())

# remote_conn.connect('localhost', port=6379)
resp = remote_conn.recv(1024).decode('ascii').split(',')
print(resp)
print(''.join(resp))
remote_conn.close()
conn.close()
# r = redis.StrictRedis(host='206.72.203.244', port=50934, password='Mangodog21', db=0)
# r.ping()
# print('Connected!')
# print(r.dbsize())