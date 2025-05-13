import sys


#global constants which will determine the number of attempts according to difficulty
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
#welcoming statement
print('WELCOME TO GUESSING NUMBER GAME')


#importing random to generate random number to be guessed later
import random as dt


status=True
attempts=0
difficulty=input('which difficulty level hard or easy ')

if difficulty=='easy':
    attempts =EASY_LEVEL_TURNS
    print('you have 10 attempts to get the guess the number right')
elif difficulty=='hard':
    attempts=HARD_LEVEL_TURNS
    print('you have 5 attempts to get the guess the number right')
else:
    print('enter from given difficulty word for word either easy or hard...run program again')
    status=False


num=dt.randrange(1,100)

while status:

    guess=int(input('enter your guess '))
    attempts-=1
    def randomizer():
        if attempts==0:
            global status
            status=False
            print(f'you didn\'t get it write and your have no more attempts')
        elif guess==num:
            status=False
            return f'you win after {EASY_LEVEL_TURNS-attempts} attempts'
        elif guess>num:
            return f'too high... you have {attempts} remaining'
        elif guess<num:
            return f'too low... you have {attempts} remaining'





    print(randomizer())


