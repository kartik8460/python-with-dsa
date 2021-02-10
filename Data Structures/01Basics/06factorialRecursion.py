def factorialRecursion(n):
    if n == 1:
        return 1
    else:
        return n*factorialRecursion(n-1)


number = int(input('Enter a Number: '))

if number < 0:
    print("No Negative Allowed")
elif number == 0:
    print("Factorial is : 1")
else:
    print("Factorial is :", factorialRecursion(number))
