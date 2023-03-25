def verifPresence(element, list):
    if (list.count(element) > 0):
        return True
    return False

print (verifPresence(2, [1, 2, 3, 4, 5, 6]))
print (verifPresence(-1, [1, 2, 3, 4, 5, 6]))
