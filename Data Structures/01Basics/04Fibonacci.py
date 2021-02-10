def fibonacci(number):
    first = 0
    second = 1
    print(first, end=" ")
    print(second, end=" ")
    for i in range(3, number + 1):
        third = first + second
        first = second
        second = third
        print(third, end=" ")


number = int(input('Enter a Number: '))
fibonacci(number)
