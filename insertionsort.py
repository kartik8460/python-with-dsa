def insertionSort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while(j >= 0 and lst[j] > key):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


lst = [5, 4, 1, 2, 6, 7, 9]
result = insertionSort(lst)
print(result)
