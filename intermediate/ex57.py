def numberOfMatch(lst):
    ret = []
    for x in lst:
        lst_tuple = (x, lst.count(x))
        if lst_tuple not in ret:
            ret.append(lst_tuple)
    return ret

print(numberOfMatch([-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1]))
print(numberOfMatch(["a", 3, 4, "b", "a", 3]))
