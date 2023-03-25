def concatList(l1, l2, l3):
    for x in l2:
        l1.append(x)
    for y in l3:
        l1.append(y)
    return l1

print(concatList([0, 9, 8], [3, 4, 2], ["false", "true", 5]))
