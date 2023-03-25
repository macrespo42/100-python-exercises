def addElementDict(key, value, dict):
    dict[key] = value
    return dict

print(addElementDict("baptiste", 29, {"julien": 14, "laurent": 31}))
print(addElementDict("weight", 65.3, {}))
