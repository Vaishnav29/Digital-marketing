# infix to postfix conversion a+b*(c^d-e)^(f+g*h)-i
operators = set(['+', '-', '*', '/', '(', ')'])
priority = {'+':1, '-':1, '*':2, '/':2}

def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in operators:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[ch] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack: output += stack.pop()
    #print(output)
    return output

str1 = input("Enter an infix expression ")    
result = infix_to_postfix(str1)
print(result)

# infix to prefix conversion (a-b/c)*(a/k-l)
operators = set(['+', '-', '*', '/', '(', ')'])
priority = {'+':1, '-':1, '*':2, '/':2}

def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in operators:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and priority[ch] <= priority[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    #print(exp_stack[-1])
    return exp_stack[-1]

str1 = input("Enter an infix expression ")    
result = infix_to_prefix(str1)
print(result)