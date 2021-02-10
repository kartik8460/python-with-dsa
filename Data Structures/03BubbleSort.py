def BubbleSort(lst):
    length = len(lst)
    for i in range(length-1):
        for j in range(length-i-1):
            if(lst[j] > lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst


lst = [5, 3, 8, 6, 7, 2]
print(BubbleSort(lst))
