def checkUpper(str):
    for x in str:
        if x.isupper():
            return True
    return False

print(checkUpper("Vegetables are good for health"))
print(checkUpper("i learn ruby"))
