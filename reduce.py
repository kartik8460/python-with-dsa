from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
addNums = reduce(lambda a, b: a+b, nums, 0)

print(addNums)
