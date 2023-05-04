result = []
for x in range(100, 999):
    x_stringified = str(x)
    sum = int(x_stringified[0]) + int(x_stringified[1]) + int(x_stringified[2])
    product = int(x_stringified[0]) * int(x_stringified[1]) * int(x_stringified[2])
    if product % sum == 0:
        result.append(x)

print(result)
