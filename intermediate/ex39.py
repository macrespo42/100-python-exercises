def maximum(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max
