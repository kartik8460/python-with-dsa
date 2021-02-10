def SelectionSort(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i, len(lst)):
            if(lst[minpos] > lst[j]):
                minpos = j
        temp = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = temp
    return lst


lst = [5, 3, 8, 6, 7, 2]
print(SelectionSort(lst))
