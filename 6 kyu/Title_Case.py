def title_case(title, minor_words=''):
    temp = title.split(" ")
    sentence = []
    words = minor_words.split(" ")
    words = [x.lower() for x in words]
    for x in temp:
        if(len(sentence)==0):
                sentence.append(x[0:1].upper()+x[1:].lower())
        else:
            if x.lower()  in words:
                sentence.append(x.lower())
            else:
                sentence.append(x[0:1].upper()+x[1:].lower())

                
    return " ".join(sentence)
