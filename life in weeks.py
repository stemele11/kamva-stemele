name=input('what\'s your name ? ')
age=int(input('how old are you ? '))

weeks_left=int((90*52)-(age*52))
days_left=int((90*365)-(age*365))
months_left=int((90*12)-(age*12))

print(f'hello {name } you are left with {months_left} months {weeks_left} weeks {days_left} days left before turning 90')



