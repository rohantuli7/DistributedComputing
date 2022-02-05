from datetime import datetime

import Pyro4
import os
@Pyro4.expose
class file_handling(object):
    def handling(self, text):
        path='/Users/rt/Desktop/rmi'

        file=open(path+'/'+text,'r')
        print(file.read())

        file = open(path + '/' + text, 'a')
        upd = input('Enter content to be appended to file: ')
        file.write(upd)
        file.close()

        file = open(path + '/' + text, 'r')
        print(file.read())

        now = datetime.now()
        print(f'{text} - file updated at {now:%H:%M:%S} \n')

def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(file_handling)
    ns.register('mess.server', str(uri))
    print(f'Ready to listen')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
