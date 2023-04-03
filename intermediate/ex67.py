try:
    lst_length = int(input("Enter list size: "))
except:
    print("Bad input")
    exit()
lst = []
for x in range(0, lst_length):
    lst.append(input("enter a list element : "))

print(lst)
