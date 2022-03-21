def filter_list(l):
    array = []
    for x in range (0, len(l)):
        if type(l[x]) == int:
            array.append(l[x])
    return array
