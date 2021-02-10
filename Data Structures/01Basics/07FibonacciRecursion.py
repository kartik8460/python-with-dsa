def fibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacciRecursion(n-1) + fibonacciRecursion(n-2))


count = int(input('Please Enter a Number: '))
fibonacciRecursion(count)

if count <= 0:
    print("Please Enter a Positive Number")
else:
    for i in range(count):
        print(fibonacciRecursion(i), end=" ")
