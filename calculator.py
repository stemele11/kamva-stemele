
import math
print('WELCOME TO CALCULATOR PROGRAM'.lower().title())
num1=float(input('enter first value to use in calculation : '))
operand=input('chose operand : \n \\ \n * \n + \n - \n % \n  ')
num2=float(input('enter second value to use in calculation : '))
result=0

use=True
print('KAMVA'.lower().title())

def calculate(num1,num2,operation):

        if operation=='+':
            result=num1+num2
            return result
        elif operation=='-':
            result=num1-num2
            return result
        elif operation=='/':
            result=num1/num2
            return result
        elif operation=='%':
            result=num1%num2
            return result
        elif operation=='*':
            result=num1*num2
            return result




while use:
    result=calculate(num1=num1,num2=num2,operation=operand)
    print(f'{num1} {operand} {num2} = {round(result,1)}')
    another=input('do you want to perform another calculation ? yes or no ')
    if another=='no':
        use=False
    else:
        answer_reuse=input('do you want to use this answer in the next calculation yes or no  ')
        if answer_reuse=='yes':
            num1=result
            num2=float(input('enter the second number  '))
            operand=input('pick operation  ')
        else:
            num1=float(input('enter first number'))
            operand=input('pick operation  ')
            num2=float(input('enter the second number  '))












