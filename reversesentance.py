def reversesentence(sent):
    word = sent.split()
    l = 0
    r = len(word)-1
    while l < r:
        word[l], word[r] = word[r], word[l]
        l+=1
        r-=1
    return " ".join(word)

print(reversesentence("Bunch Of Bull"))