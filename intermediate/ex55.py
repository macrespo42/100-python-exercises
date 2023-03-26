def filterWord(sentence, minLen):
    sentence_lst = sentence.split(' ')
    return [x for x in sentence_lst if len(x) > minLen]

print(filterWord("Salut toi", 4))
print(filterWord("Quel est ton origine ?", 5))
