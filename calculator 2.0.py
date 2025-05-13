from zoneinfo import reset_tzpath

num1=float(input('enter first number '))
operand=input('which operand \n+\n-\n*\n%\n/\n')
num2=float(input('enter number second number '))



def add(num1,num2):
    return num1 + num2
def minus(num1,num2):
    return num1 - num2
def divide(num1,num2):
    return num1 / num2
def multiply(num1,num2):
    return num1 * num2
def modula(num1,num2):
    return num1 % num2

operations={
    '-':minus,
    '/':divide,
    '*':multiply,
    '+':add,
    '%':modula,

}
again=True

while again:
    for do in operations:
        if do==operand:
            result=operations[do]
            print(result(num1,num2))
            again = input('do you want to perform another calculation true or false ').lower().title()



            if again=='True':
                reuse=input('do you want to use answer in the next calculation yes or no ').lower()
                if reuse=='yes':
                    again=True
                    num1=result(num1,num2)
                    num2=float(input('enter second number '))
                    operand=input('enter operand ')
                    if do==operand:
                        result=operations[do]
                        x=result(num1,num2)
                        #print(x)
                else:
                    num1=float(input('enter first number '))
                    num2=float(input('enter second number '))
                    operand=input('enter operation ')
                    if do==operand:
                        result=operations[do]
                        x=result(num1,num2)
                        print(x)

            else:
                again=False















