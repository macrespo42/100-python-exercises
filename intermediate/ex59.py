def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

print(gcd(3, 5))
print(gcd(5, 15))
