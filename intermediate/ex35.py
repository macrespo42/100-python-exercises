def sumOfEachNumber(nb):
    nbStr = str(nb)
    sum = 0
    for elt in nbStr:
        sum += int(elt)
    print (sum)
