import socket

path_c = '/Users/rt/Desktop/College/4th year/sem 7/DC/Experiments/exp6/client/client.txt'
path_s = '/Users/rt/Desktop/College/4th year/sem 7/DC/Experiments/exp6/server/server.txt'

s = socket.socket()
port = 12345
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
c, addr = s.accept()


def func_read():
    file = open(path_s, 'r')
    print('Data in file : ')
    print(file.read())


def func_write():
    file_c = open(path_c, 'a+')
    file_s = open(path_s, 'a+')
    text = input('Enter text to be inserted into the file : ')
    text = '\n' + text
    file_c.write(text)
    file_s.write(text)
    file_s.close()
    file_c.close()
    file = open(path_s, 'r')
    print('Text in file :\n', file.read())


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