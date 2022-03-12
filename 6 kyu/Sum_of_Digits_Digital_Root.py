def digital_root(n):
    while(len(str(n))>1):
        temp=0
        for x in str(n):
            temp += int(x)
        n = temp
        if(len(str(n))<1):
            break
    return n
