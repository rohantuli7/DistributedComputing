import random

n = input('Enter number of Processes present : ')
r = random.sample(range(0,100),int(n))
r.sort()
print('Processes present in the pipeline : {}'.format(r))
c = random.choice(r)
print('The coordinator is : ',c)
rt = []

while True:
    l = [i for i in r if i>c]
    print()
    print('Processes present in the system : {}'.format(l))
    for i in l:
        print('Message sent to {}'.format(i))
    print()
    for i in l:
        print()
        print('Does Process {} want  to participate?'.format(i))
        ip = int(input('Press 1. Yes or 2. No '))
        if ip == 1 and rt.count(i) == 0:
            rt.append(i)
        else:
            pass

    if len(rt) == 1:
        print('The coordinator is : ',rt[0])
        break
    elif len(rt) == 0:
        print('The coordinator is :',c)
        break
    else:
        c = rt[0]
    c = rt[0]
    r = rt
