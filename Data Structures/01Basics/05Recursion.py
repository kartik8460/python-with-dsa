def recursion1(n):
    if(n > 0):
        print('Recursion1 -', n)
        recursion1(n-1)


recursion1(3)

print('*************************************')


def recursion2(n):
    if(n > 0):
        recursion2(n-1)
        print('Recursion2 -', n)


recursion2(3)
print('*************************************')


def recursion3(n):
    if(n > 0):
        print('Recursion3 -', n)
        recursion3(n-1)
        recursion3(n-1)


recursion3(3)
print('*************************************')


def recursion4(n):
    if(n > 0):
        recursion4(n-1)
        recursion4(n-1)
        print('Recursion4 -', n)


recursion4(3)
print('*************************************')


def recursion5(n):
    if(n > 0):
        recursion5(n-1)
        print('Recursion5 -', n)
        recursion5(n-1)


recursion5(3)
