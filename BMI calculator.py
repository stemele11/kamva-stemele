name=input('what is your name :   ')
height=float(input('what is your current height in meters ?  '))
weight=float(input('what is your current weight in kg?  '))

bmi=int(weight/(height**2))


if bmi<18.5:
    print(f'{name} you BMI is {bmi} and it shows that you are underweight')
elif bmi>=18.5 and bmi<25:
    print(f'{name} you BMI is {bmi} and it shows that you are normal weight')
elif bmi>=25 and bmi<30:
    print(f'{name} you BMI is {bmi} and it shows that you are overweight')
elif bmi>=30 and bmi<35:
    print(f'{name} you BMI is {bmi} and it shows that you are obese')
else:
    print(f'{name} you BMI is {bmi} and it shows that you are clinically obese')

