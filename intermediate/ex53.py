def deleteSpace(sentence):
    ret = sentence.split(' ')
    ret = ''.join(ret)
    return ret

print(deleteSpace("go to the plage"))
