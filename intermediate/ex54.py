def positionEltList(lst, x):
    lst_positions = []
    for i in range(len(lst)):
        if lst[i] == x:
            lst_positions.append(i)
    if len(lst_positions) == 0:
        print(f"{x} is not present in lst {lst}")
    return lst_positions

print(positionEltList([1, 2, 3], 4))
print(positionEltList([1, 2, 3], 3))
