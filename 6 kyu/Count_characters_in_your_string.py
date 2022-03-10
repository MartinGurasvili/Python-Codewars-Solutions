def count(string):
    dict ={}
    for x in string:
        if x in dict:
            dict.update({x: dict.get(x)+1})
        else:
            dict[x] = 1
    return dict
