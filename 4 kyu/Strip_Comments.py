def solution(string,markers):
    temp = string.split("\n")
    for x in range(len(temp)):
        for y in markers:
            while y in temp[x]:
                if(y in temp[x] ):
                    temp[x]= (temp[x][:temp[x].index(y)-1])
                else:
                    break

    
    return "\n".join(temp) if "\n".join(temp)[len("\n".join(temp))-1:len("\n".join(temp))] != " " else "\n".join(temp)[:-1]
