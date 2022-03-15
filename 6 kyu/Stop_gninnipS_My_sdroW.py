def spin_words(sentence):
    f=[]
    sentence = sentence.split(" ")
    for y in sentence:
        if(len(y) >=5):
            l=[]
            for x in range(len(y)-1,-1,-1):
                l.append(y[x])
            f.append("".join(l))
        else:
            f.append(y)
    return " ".join(f)
