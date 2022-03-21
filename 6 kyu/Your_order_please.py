def order(sentence):
    if(sentence != ""):
        sentence= sentence.split(" ")
        end_array = [None] * len(sentence)
        for x in range (0, len(sentence)):
            for i in range(0, len(sentence[x])):
                if (str(sentence[x])[i].isnumeric()):
                    end_array[int(str(sentence[x])[i])-1] = sentence[x]
        return (" ".join(end_array))
    else:
        return sentence
