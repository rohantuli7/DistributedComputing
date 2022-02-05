from datetime import datetime

import Pyro4
server = Pyro4.Proxy(f"PYRONAME:mess.server")

def start_chatting():
    text = ''
    while (text != 'exit'):
        text = input("Enter the file name to be updated: ")
        now = datetime.now()
        server.handling(text)
        print(f'Request sent at {now:%H:%M:%S} \n')

if __name__ == '__main__':
    try:
        start_chatting()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
