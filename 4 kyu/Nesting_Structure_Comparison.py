def same_structure_as(original,other):
    count = 0
    if(type(original)==type(other)):
        if(len(original)==len(other)):
            for x in range(len(original)):
                if(type(original[x])==type(other[x])):
                    if(isinstance(original[x], list)):
                        try:
                            if(len(original[x]) == len(other[x])):
                                print(len(original[x]), len(other[x]))
                                if(type(original[x][0])==type(other[x][0])):
                                    count+=1
                        except:
                             count+=1
                    else:
                        count+=1
                else:
                    if(isinstance(original[x], list)==isinstance(other[x], list)):
                        count+=1
                    
    else:
        return False
    return True if count==len(other) else False
