import random

def passwordGenerator(chars, pass_size):
    password = ""
    for i in range(0, pass_size):
        password += chars[random.randint(0, len(chars) - 1)]
    return password

print(passwordGenerator("hiufdsgad", 12))
