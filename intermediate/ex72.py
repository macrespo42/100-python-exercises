def calcSum(lst):
    sum = 0
    for x in lst:
        if type(x) == list:
            sum += calcSum(x)
        else:
            sum += x
    return sum

print(calcSum([7, 8, [1, 2, 3], [14]]))
