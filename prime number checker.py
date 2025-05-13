num=int(input('enter number '))
def prime_checker(number):
    if number%2==1:
        print(f'{number} is not a prime number')
    else:
        print(f'{number} is a number')


prime_checker(num)
