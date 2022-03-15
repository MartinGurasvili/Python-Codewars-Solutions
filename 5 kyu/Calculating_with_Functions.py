def operation(op,num1,num2):
    if(op=='times'):
        return num1*num2
    if(op=='plus'):
        return num1+num2
    if(op=='minus'):
        return num1 -num2
    if(op=='divided_by'):
        return int(num1 /num2)

def zero(op = None):
    if op != None:
        return operation(op[1],0,op[0])
    else:
        return 0
def one(op = None):
    if op != None:
        return operation(op[1],1,op[0])
    else:
        return 1
def two(op = None):
    if op != None:
        return operation(op[1],2,op[0])
    else:
        return 2
def three(op = None):
    if op != None:
        return operation(op[1],3,op[0])
    else:
        return 3
    
def four(op = None):
    if op != None:
        return operation(op[1],4,op[0])
    else:
        return 4
    
def five(op = None):
    if op != None:
        return operation(op[1],5,op[0])
    else:
        return 5
    
def six(op = None):
    if op != None:
        return operation(op[1],6,op[0])
    else:
        return 6

def seven(op = None):
    if op != None:
        return operation(op[1],7,op[0])
    else:
        return 7

def eight(op = None):
    if op != None:
        return operation(op[1],8,op[0])
    else:
        return 8
    
def nine(op = None):
    if op != None:
        return operation(op[1],9,op[0])
    else:
        return 9
    
def plus(num):
    oper = 'plus'
    return num,oper
def minus(num):
    oper = 'minus'
    return num,oper
def times(num): 
    oper = 'times'
    return num,oper
def divided_by(num):
    oper = 'divided_by'
    return num,oper
