import random

def find_higher(h, m):
    return [local_machine for local_machine in m if h < local_machine]


def send_requests(h, m):
    for local_machine in m:
        if h != local_machine:
            print(f'{h} sent request to {local_machine}')


def send_response(h, m):
    for local_machine in m:
        if h != local_machine:
            print(f'{local_machine} sent response to {h}')


def find_remaining(k, l):
    k = set(k)
    l = set(l)
    m = list(k - l)
    return m


machines = []
n = int(input('Enter number of machines: '))

for i in range(n):
    random_id = random.randint(100, 1000)
    while random_id in machines:
        random_id = random.randint(100, 1000)

    machines.append(random_id)

print('Enter an ID which is holding election out of', machines)
holder = int(input())

temp_machines = [0] * n
temp_machines[:] = machines

holders = [holder]

temp = find_higher(holder, machines)

if len(temp) == 0:
    print(f'{holder} is the new coordinator')

else:
    send_requests(holder, temp)

    print('The remaining IDs are:', temp)
    exclusions = list(map(int, input('Enter the IDs who will not respond: ').split(' ')))

    rem = find_remaining(temp, exclusions)
    send_response(holder, rem)

    holders = sorted(rem)
    if len(holders) == 0:
        print(f'{holder} is the new coordinator')
    i = 0
    while len(holders) > 0:
        temp = find_higher(holders[0], machines)
        if len(temp) == 0:
            print(f'{holders[0]} is the new coordinator')
            break
        else:
            send_requests(holders[0], temp)

            print('The remaining IDs are:', temp)
            exclusions = list(map(int, input('Enter the IDs who will not respond : ').split(',')))

            rem = find_remaining(temp, exclusions)

            holders = sorted(rem)

            if len(holders) == 1:
                print(f'{holders[0]} is the new coordinator')
                break
            else:
                send_response(holders[0], rem)
