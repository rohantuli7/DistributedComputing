

#read
#file = open("/Users/rt/Desktop/dc_1-1.txt","r")
#s = file.read()

#write
#f = open("/Users/rt/Desktop/dc_1-2.txt", "w")
#f.write(togu)

import socket


path_c = '/Users/rt/Desktop/College/4th year/sem 7/DC/Experiments/exp6/client/client.txt'
path_s = '/Users/rt/Desktop/College/4th year/sem 7/DC/Experiments/exp6/server/server.txt'

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
s.close()
print('Client connected to server')



def func_read():
    file = open(path_c,'r')
    print('Data in file : ')
    print(file.read())

def func_write():
    file_c = open(path_c,'a+')
    file_s = open(path_s,'a+')
    text = input('Enter text to be inserted into the file : ')
    text = '\n' + text
    file_c.write(text)
    file_s.write(text)
    file_s.close()
    file_c.close()
    file = open(path_c, 'r')
    print('Text in file :\n',file.read())

while True:
    ip = int(input('Enter choice 1. Read 2. Write 3. Exit '))
    if ip == 1:
        func_read()
    elif ip == 2:
        func_write()
    elif ip == 3:
        break
    else:
        print('Incorrect input!')