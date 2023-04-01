import os

def nbrFiles(dirPath):
    content = os.listdir(dirPath)
    files = 0
    for element in content:
        if os.path.isfile(os.path.join(dirPath, element)):
            files += 1
    return files

print(nbrFiles("./ressources"))
