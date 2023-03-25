def dictValuesLength(dict):
    length = 0
    for value in dict.values():
        length  += len(value)
    return length  

print(dictValuesLength({"a": [1, 2, 3], "b": [4], "c": []}))
