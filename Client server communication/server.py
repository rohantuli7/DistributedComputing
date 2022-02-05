while True:
    print('Enter type of communication')
    user_input = int(input('1. Substitution 2. Transposition : '))

    import socket
    if user_input == 1:
        s = socket.socket()
        port = 12345
        s.bind(('', port))
        print()
        print("socket binded to %s" % (port),' \n')

        s.listen(5)

        c, addr = s.accept()
        x = c.recv(1024).decode()
        print('File received. Data in file : ',x)
        print()

        y = c.recv(1024).decode()
        print('Key received. Value : ',y)

        def get_key(val):
            for key, value in d.items():
                if val == value:
                    return key

            return "key doesn't exist"


        key = int(y)
        d = {}
        count = 0
        for i in range(97,123):
            count = count + 1
            temp = chr(i)
            d[temp] = count
        togu = ''
        rt = x.lower()
        for i in rt:
            if i in d:
                temp = d[i] + key
                if temp > 26:
                    temp = temp - 26
                    t = get_key(temp)
                    togu = togu + t
                else:
                    t = get_key(temp)
                    togu = togu + t
            elif i == ' ':
                togu = togu + '$'

        print()
        print('File after encryption : ',togu)

        f = open("/Users/rt/Desktop/dc_1-2.txt", "w")
        f.write(togu)
        f.close()

        s.close()
        break

    elif (user_input == 2):
        s = socket.socket()
        port = 12346
        s.bind(('', port))
        print()
        print("socket binded to %s" % (port),' \n')

        s.listen(5)

        c, addr = s.accept()
        x = c.recv(1024).decode()
        print('File received. Data in file : ',x)
        print()

        def remove_spaces(s):
            return "".join(s.split())

        rt = x
        new_rt = remove_spaces(rt)
        l = len(new_rt)

        n = 0
        for i in range(1,101):
            if i*i > l:
                n = i
                break

        a = n*n - l
        if a>0:
            for i in range(a):
                new_rt = new_rt + '$'
        togu = [[] for i in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                togu[i].append(new_rt[count])
                count = count + 1
        new_str = ''

        for i in range(n):
            for j in range(n):
                new_str = new_str + togu[j][i]

        print('File after encryption : ',new_str)

        f = open("/Users/rt/Desktop/dc_2-2.txt", "w")
        f.write(new_str)
        f.close()
        s.close()
        break
    else:
        print('Incorrect User input')