def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


number = int(input('Enter a Number: '))

if number < 0:
    print("No Negative Allowed")
elif number == 0:
    print("Factorial is : 1")
else:
    print("Factorial is :", factorial(number))
