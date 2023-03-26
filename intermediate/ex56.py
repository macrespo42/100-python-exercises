def reverseSentence(sentence):
    l = sentence.split(' ')
    l.reverse()
    l = ' '.join(l)
    return l

print(reverseSentence("Hello my friends"))
