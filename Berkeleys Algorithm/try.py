import datetime
timestr = '12:00:00'
ftr = [3600, 60, 1]
x = sum([a * b for a, b in zip(ftr, map(int, timestr.split(':')))])
print(x)
print(datetime.timedelta(seconds = x))

address = []
time = []
client_time = []
while True:
    c, addr = s.accept()
    address.append(c)
    print('Got connection from', addr)
    t = c.recv(1024).decode()
    time.append(int(t))
    ex = input('Press 1 to exit : ')
    if ex == '1':
        break
    else:
        pass
sum1 = 0
n = len(time) + 1
print(time)
for i in time:
    sum1 = sum1 + i

sum1 = (sum1/n)*-1

sync_time = sum1 + int(sectime)
