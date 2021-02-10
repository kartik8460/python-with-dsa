def reverseString1(string):
    return string[::-1]


def reverseString2(string):
    reverseStr = ''
    for i in string:
        reverseStr = i + reverseStr
    return reverseStr


string = input('Enter a string: ')
print(reverseString1(string))
print(reverseString2(string))
