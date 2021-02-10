def binarySearch(lst, n):
    st = 0
    end = len(lst)-1
    pos = -1
    while(st <= end):
        mid = (st+end)//2
        if(lst[mid] == n):
            pos = mid
            return True, pos
        else:
            if(lst[mid] < n):
                st = mid + 1
            else:
                end = mid - 1
    return False


n = 99
lst = [4, 7, 8, 12, 45, 99]
print(binarySearch(lst, n))
