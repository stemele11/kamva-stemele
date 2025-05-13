number =int(input('enter a number the count should end  '))

'''if number is divisible by 3 and 5 we print Fizzbuzz.
    if only divisible by 3 print Fizz
    else if only divisible  by 5 print Buzz'''

for i in range(1,number+1):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

