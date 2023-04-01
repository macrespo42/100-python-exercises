def hasNumber(filePath):
    file = open(filePath, "r")
    content = file.readlines()
    content = "".join(content)
    return any(chr.isdigit() for chr in content)

print(hasNumber("./ressources/ex62.txt"))
