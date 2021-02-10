def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


print('***********************************************')

values = topten()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print('***********************************************')


def topten2():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1


values2 = topten2()

for i in values2:
    print(i)

print('***********************************************')
