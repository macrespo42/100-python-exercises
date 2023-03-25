def minimum(lst):
    min = lst[0]
    for x in lst:
        if min > x:
            min = x
    return min

print(minimum([-9, 2, 4, 1, 8]))
print(minimum([-3, 1, 7, 6, 2, 3]))
