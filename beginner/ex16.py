l1 = [9, 8, 7, 14, 3, 2, "a", "p", "bonjour", "b"]
l2 = ["b", 1, 9.2, 6, 3, 9, "p"]

# list comprehension solution
# l3 = [x for x in l1 if l2.count(x) > 0]

# set solution (cleaner IMO)
l3 = set(l1).intersection(set(l2))

print(list(l3))
