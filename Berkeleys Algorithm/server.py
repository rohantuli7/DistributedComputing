import socket
import datetime

s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")

stime = input('Enter server time : ')

timestr = stime
ftr = [3600, 60, 1]
sectime = sum([a * b for a, b in zip(ftr, map(int, timestr.split(':')))])

address = []
time = []
while True:
    c, addr = s.accept()
    address.append(c)
    print('Got connection from', addr)
    temp = int(c.recv(1024).decode())
    time.append(temp)
    ex = input('Press 1 to exit : ')
    if ex == '1':
        break
    else:
        pass

diff = []
for i in time:
    temp = sectime - i
    diff.append(temp)

sum1 = 0
n = len(diff) + 1
for i in diff:
    sum1 = sum1 + i

sum1 = (sum1/n)*-1
sync_time = sum1 + int(sectime)

indv = []
for i in time:
    temp = sync_time - i
    indv.append(temp)

for i,j in zip(address,indv):
    i.send(str(j).encode())

print('Synchronized time = {}'.format(datetime.timedelta(seconds = sync_time)))