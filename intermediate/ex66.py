def keyMaxValue(dict):
    max = list(dict.keys())[0]
    maxLen = 0
    for k, v in dict.items():
        vLen = len(set(v))
        if vLen > maxLen:
            maxLen = vLen
            max = k
    return max

print(keyMaxValue({"a": [9, 10, 9, 7, 3, 1], "b": [5, 3, 2, 2, 2], "c": [1, 1, 1, 1, 1, 1, 8, 2]}))
