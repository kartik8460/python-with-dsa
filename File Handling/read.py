f1 = open('read.txt', 'r')
print(f1.read())

f2 = open('demo.txt', 'r')
print(f2.readline(), end="")
print(f2.readline(), end="")
print(f2.readline(), end="")

f1.close()
f2.close()
