def unionLst(lst1, lst2, lst3):
    ret = set(lst1).union(lst2).union(lst3)
    return sorted(ret)

print(unionLst([3, 6, 9, 3], [1, 0, 3], [12, 6, 0]))
