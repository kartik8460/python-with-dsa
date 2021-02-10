def powerRecursion(base, power):
    if power == 1:
        return base
    else:
        return base * powerRecursion(base, power-1)


number = int(input('Enter the Number: '))
power = int(input('Enter the Power: '))

print(number, 'to the power', power, 'is :', powerRecursion(number, power))
