def concatDict(d1, d2):
    for key in d2:
        d1[key] = d2[key]
    return d1 

print(concatDict({"a": 3, "b": 6}, {"c": 2, "d": 4}))
