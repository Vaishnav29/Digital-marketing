# evaluate infix expression
result = eval('(1 + ( ( 2 + 3)  *  ( 4 * 5 )  ) )')
print("result of (1 + ( ( 2 + 3)  *  ( 4 * 5 )  ) ) is",result)

# evaluation of postfix expression
def push(l, item):
    l.append(item)
    
def pop(l):
    if(len(l)!=0):
        return l.pop()
    else:
        return
    
stack = []
expr = []
    
def evalpost(post):
    for i in range(len(post)):
        if(post[i]!=' '):
            push(stack, str(post[i]))
        
    for i in stack:
        if i in "0123456789":
            push(expr, i)
        else:
            if(len(expr) >= 2):
                operand2 = pop(expr)
                operand1 = pop(expr)
                result = doMath(i,operand1,operand2)
                push(expr, result)
    return pop(expr)

def doMath(op, op1, op2):
    if op == "*":
        return float(op1) * float(op2)
    elif op == "/":
        return float(op1) / float(op2)
    elif op == "+":
        return float(op1) + float(op2)
    else:
        return float(op1) - float(op2)

str1 = input("Enter a postfix expression ")    
result = evalpost(str1)
print(result)


# evaluation of prefix expression
operators = set(['+', '-', '*', '/', '(', ')'])
priority = {'+':1, '-':1, '*':2, '/':2}

def evalpre(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps)-2):
            if exps[i] in operators:
                if not exps[i+1] in operators and not exps[i+2] in operators:
                    op, a, b = exps[i:i+3]
                    a,b = map(float, [a,b])
                    c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[op]
                    exps = exps[:i] + [c] + exps[i+3:]
                    break
        #print(exps)
    return exps[-1]

str1 = input("Enter a prefix expression ")    
result = evalpre(str1)
print(result)
