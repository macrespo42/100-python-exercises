def factorial(nb):
    if nb == 0:
        return 0
    total = nb
    while nb > 1:
        nb -= 1
        total *= nb
    return total

print(factorial(9))
