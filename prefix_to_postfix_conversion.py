def Conversion(expression):
    
    stack =[]

    operators = set(['+', '-', '/','*'])

    s = expression[::-1]

    for i in s:
        if i in operators:
            
            a = stack.pop()
            b  = stack.pop()

            temp = a + b + i
            stack.append(temp)
        
        else:
            stack.append(i)

    print(*stack)


Conversion("*-A/BC-/AKL")

'''COVERSION

1 ) prefic to postfix - if operator push to operators and then push op1+op2+operator else push operand

2 ) Postfix to Prefix - if operator push to operators and then push operartor + op1+op2 else push operand

3 ) postfix to infix - if operator push ( op2 + operator + op1) else push operand

'''

