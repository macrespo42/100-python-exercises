def getNumberOfFruits(fruits):
   return fruits[1] 

l = [("Pomme", 15), ("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Peche", 2)]
l.sort(key=getNumberOfFruits)
print(l)
