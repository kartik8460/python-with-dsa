a = int(input('Enter a number: '))
b = int(input('Enter a number greater than 0: '))

try:
    print(a/b)
except ZeroDivisionError as e:
    print('Hey Cannot divide a number by 0')
    print(e)
finally:
    print('Wheather there is a successfull try or and Exception accepted. Finally Always Run :)')
