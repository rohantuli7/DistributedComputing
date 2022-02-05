import socket
server = socket.socket()
port = 12345
server.connect(('127.0.0.1', port))
print('Client connected')
file = open("/Users/rt/Desktop/dc_1-1.txt","r")
s = file.read()
server.send(s.encode())
ip = input('Give key value : ')
server.send(ip.encode())
server.close()
