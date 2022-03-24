def array_diff(a, b):
    end = []
    for x in b:
        end = [x for x in a if x not in b]
        print(end)
    if(end == []):
        return(a)
    else:
        return(end)
