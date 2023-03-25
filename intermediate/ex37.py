def removeDuplicate(lst):
    ret = set(lst)
    ret = list(ret)
    ret.sort()
    return ret

print(removeDuplicate([0, 3, 5, 7, 3, 5, 1, -1]))
print(removeDuplicate([-3, -6, 0, 1, 2, 7]))
