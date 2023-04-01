def getFileContent(filePath):
    file = open(filePath, "r")
    content = file.readlines()
    file.close
    return content

def delChar(filePath, char):
    content = getFileContent(filePath)
    file = open(filePath, "w")
    new_content = "".join(content).replace(char, "")
    file.write(new_content)
    file.close

delChar("./ressources/ex62.txt", ",")
print(getFileContent("./ressources/ex62.txt"))
