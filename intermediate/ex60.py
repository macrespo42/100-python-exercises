def readFile(filePath):
    file = open(filePath, "r")
    return file.read()

print(readFile("./ressources/ex60.txt"))
