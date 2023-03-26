def includeVowel(sentence):
    vowels = ["a", "e", "i", "o", "u", "y"]
    for v in vowels:
        if sentence.count(v) > 0:
            return True
    return False

print(includeVowel("I'm gonna take my shower"))
print(includeVowel("rbhpm"))

