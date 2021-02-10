arr = [5, 8, 4, 6, 9, 2]

n = 9

pos = -1


def search(arr, n):
    i = 0
    while(i < len(arr)):
        if(arr[i] == n):
            globals()['pos'] = i
            return True
        i += 1
    return False


if(search(arr, n)):
    print('Found at', pos)
else:
    print('Not Found')
