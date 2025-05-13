import random as dt

done=False
names=[]
name=input('enter your name  ')
names.append(name)
while done==False:
    more=input('is there another name to be entered y/n  ')
    if more=='y':
        name=input('enter your name  ')
        names.append(name)
    elif more=='n':
        done=True
        paying=dt.choice(names)
        print(f'{paying} is settling the bill')
        print(names)



