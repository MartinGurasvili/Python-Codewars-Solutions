def persistence(n):
    count = 0
    while len(str(n)) > 1:
        num = 1
        for x in (str(n)):
            num = num *int(x)
        count +=1
        n = num
    return(count)
