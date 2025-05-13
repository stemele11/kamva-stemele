import  random as dt

names=input('enter names of everyone separated by a comma ')
namesL=names.split(',')
paying =dt.randint(0,(len(namesL)-1))
print(f'{namesL[paying]} is settling the bill')