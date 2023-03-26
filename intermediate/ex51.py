def dividerMult(n, a, nbRange):
    dividers = []    
    for x in range(1, nbRange):
        if (x % n == 0) and not (x % a == 0):
            dividers.append(x)
    return dividers

print(dividerMult(5, 2, 100))
print(dividerMult(11, 3, 85))
