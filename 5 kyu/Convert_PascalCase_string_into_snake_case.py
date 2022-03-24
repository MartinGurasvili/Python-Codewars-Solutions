def to_underscore(string):
    if((str(string)).isnumeric() == False):
        ar = []
        strr= []
        print(string)
        for x in range(len(string)):
            if string[x].isupper():
                ar.append(x)
        if(ar == []):
            return(string.replace('__', '_', len(string)+1))
        else:
            string = string.lower()
            for x in range(len(ar)-1):
                strr.append(string[ar[x]:ar[x+1]])
            strr.append(string[ar[-1]:len(string)])
            return("_".join(strr))
    else:
        return (str(string))
