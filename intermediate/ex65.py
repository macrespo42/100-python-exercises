def writeFile(filePath, content):
    with open(filePath, "w") as file:
        file.write(content)

writeFile("./ressources/test.txt", "hello world\n")
with open("./ressources/test.txt", "r") as file:
    print(file.read())
