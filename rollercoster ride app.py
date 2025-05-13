height=float(input('what is your height ?  '))
age=int(input('how old are you ? '))
photo=input('do you want a photo taken y/n').lower()
bill=0

if height>120:
    print('you can ride the rollercoaster')
    photo=input('do you want a photo taken y/n').lower()
    if age<12:
        bill=5
    elif age<=18:
        bill=7
        #middle life crisis group gets free ride
    elif age>=45 and age<=55:
        bill=0
    else:
        bill=8
    if photo=='y':
        print(f'pay ${bill+3}')
    elif photo=='n':
        print(f'pay ${bill}')



else:
    print('go grow taller and come back you can\'t ride ')