def nbrOccFile(filePath, word):
    file = open(filePath, "r")
    content = file.read()
    return content.count(word)

print(nbrOccFile("./ressources/ex61.txt", "banana"))
