import random

name = ['John', 'Jack']
print('How many pencils would you like to use:')

while True:
    try:
        a = int(input())
        if a > 0:
            break
        else:
            print('The number of pencils should be positive')
    except ValueError:
        print('The number of pencils should be numeric')

print('Who will be the first (John, Jack):')
while True:
    b = input()
    if b not in name:
        print("Choose between 'John' and 'Jack'")
    else:
        break

while a > 0:
    print('|' * a)
    print(f"{b}'s turn:")
    if b == 'Jack':
        if a % 4 == 0:
            c = 3
        elif a % 4 == 3:
            c = 2
        elif a % 4 == 2:
            c = 1
        else:
            c = random.randint(1, min(3, a))
        print(c)
    else:
        while True:
            try:
                c = int(input())
                if 3 >= c > 0:
                    break
                else:
                    print("Possible values: '1', '2' or '3'")
            except ValueError:
                print("Possible values: '1', '2' or '3'")
    a -= c

    if a < 0:
        print('Too many pencils were taken')
        c = int(input())

        break

    if a == 0:
        break

    if b == 'John':
        b = 'Jack'
    else:
        b = 'John'

if b == 'John':
    b = 'Jack'
else:
    b = 'John'

print(f'{b} won!')
