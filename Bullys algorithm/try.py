import random

def genfunc():
    n = input('Enter number of Processes present : ')
    r = random.sample(range(0,100),int(n))
    return r

def election(a,b,c):
    l = c
    coordinator = b
    e = a
    e.remove(b)
    p = participation(e)
    priority(coordinator,l,p)


def participation(li):
    e = li
    temp = []
    for i in e:
        print('Message sent to {}'.format(i))
    for i in e:
        print('Does {} process want to participate?'.format(i))
        ip = int(input('Press 1. Yes or 2. No'))
        if ip == 1:
            temp.append(i)
        else:
            pass
    return temp

def priority(a,b,c):
    coor = a
    ae = b
    pe = c
    rt = []
    for i in pe:
        if coor < i:
            rt.append(i)
        else:
            pass
    rt = rt.sort()
    if len(rt) == 0:
        print('Coordinator is ',coor)
    else:
        for i in rt:


x = genfunc()
c = random.choice(x)
print('The initial coordinator is : ',c)
election(x,c,x)
