f1 = open('read.txt', 'r')
f2 = open('write.txt', 'w')


for data in f1:
    f2.write(data)
