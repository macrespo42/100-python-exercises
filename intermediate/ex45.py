def divider(nb):
    dividers = []
    x = 1
    while x <= nb:
        if nb % x == 0:
            dividers.append(x)
        x += 1
    return dividers

print(divider(9))
    
