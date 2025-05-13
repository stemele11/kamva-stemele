import random as dt
names=input('enter names of everyone involved separated by a coma')

namesL=names.split(',')
paying=dt.choice(namesL)
print(f'{paying} is chosen to settle the bill')
print(namesL)
