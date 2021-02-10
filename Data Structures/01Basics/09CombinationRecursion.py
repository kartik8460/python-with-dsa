# nCr
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def combinationRecursion(n, r):
    return (fact(n)/(fact(r) * fact(n-r)))


n = int(input('Enter the value of n: '))
r = int(input('Enter the value of: '))

print(int(combinationRecursion(n, r)))
