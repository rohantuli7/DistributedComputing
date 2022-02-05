import socket
import datetime
global rt
global val
global stime
global togu


s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")

rt = []
stime = input('Enter server time : ')
val = []
togu = []
while True:
    c, addr = s.accept()
    val.append(c)
    print('Got connection from', addr)
    rt.append(c.recv(1024).decode())
    ex = input('Press 1 to exit : ')
    if ex == '1':
        break
    else:
        pass

def berk():
    for i in togu:
        s = sum

for i in val:
    timestr = stime
    ftr = [3600, 60, 1]
    x = sum([a * b for a, b in zip(ftr, map(int, timestr.split(':')))])
    i.send(x.encode())
    temp = i.recv(1024).decode()
    togu.append(temp)







for i in val:
    i.close()
'''def berk():
    tsec = []
    n = rt.count()
    for i in rt:
        timestr = i
        ftr = [3600, 60, 1]
        x = sum([a * b for a, b in zip(ftr, map(int, timestr.split(':')))])
        tsec.append(x)

    d = tsec[0]
    diff = []
    for i in tsec:
        temp = d - i
        diff.append(temp)
    # y = datetime.timedelta(seconds=x)

    print(tsec)'''