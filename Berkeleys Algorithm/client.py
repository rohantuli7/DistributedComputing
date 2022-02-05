import socket
import datetime


def func(time):
    timestr = time
    ftr = [3600, 60, 1]
    sectime = str(sum([a * b for a, b in zip(ftr, map(int, timestr.split(':')))]))
    return sectime


s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
time = input('Enter the time of the server : ')
ctime = func(time)

s.send(ctime.encode())
ctime = int(ctime)
diff = float(s.recv(1024).decode())
togu = float(diff)
sync_time = diff + ctime
f = datetime.timedelta(seconds=sync_time)
print()
print()
print('synchronized time = {}'.format(f))
s.close()
