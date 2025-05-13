bill =0
extra_cheese=input('do you want extra cheese y/n').lower()
toppings=input('do you want pepperoni topping y/n').lower()
size=input('indicate size by either small,medium or large').lower()


if toppings=='y' and size=='small':
    bill=15+2
elif toppings=='n' and size=='small':
    bill=15

if toppings=='y' and size=='medium':
    bill=20+3
elif toppings=='n' and size=='medium':
    bill=20

if toppings=='y' and size=='large':
    bill=25+3
elif toppings=='n' and size=='large':
    bill=25

if extra_cheese=='y':
    bill+=1

print(f'final bill is ${bill}')

