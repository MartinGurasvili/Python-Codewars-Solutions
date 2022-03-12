def compute_sum(n):
    sum = 0
    for x in range (0,n+1):
        if len(str(x))>1:
            for y in str(x):
                sum+= int(y)
        else:
            sum += x
        
    return sum
