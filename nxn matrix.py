def matrix_string(n, string):
    string = string.lower()
    length = len(string)
    currentIdx = -1
    base_string = 'welcome'
    currentword = 0

    for i in range(0, length):
        if string[i] == base_string[currentword]:
            currentIdx = i
            currentword += 1
            break
    else:
        return 0

    while(currentword < len(base_string)-1):
        print(currentword, currentIdx)
        if(currentIdx + 1 < length and base_string[currentword] == string[currentIdx + 1]):
            currentIdx += 1
            currentword += 1
        elif(currentIdx - 1 > 0 and base_string[currentword] == string[currentIdx - 1]):
            currentIdx -= 1
            currentword += 1
        elif(currentIdx + n < length and base_string[currentword] == string[currentIdx + n]):
            currentIdx += n
            currentword += 1
        elif(currentIdx - n > 0 and base_string[currentword] == string[currentIdx - n]):
            currentIdx -= n
            currentword += 1
        else:
            return 0

    return 'welcome'


# n = int(input())
# string = input()
n = 4
string = 'wabgeldhocdimefj'
print(matrix_string(n, string))
