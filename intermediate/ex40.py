def sumSubList(lst, i, j):
    return sum(lst[i:j+1])

print(sumSubList([4, 10, 12 ,16, 18], 2, 4))
print(sumSubList([2, 4, 6, 8, 10, 12], 0, 2))
