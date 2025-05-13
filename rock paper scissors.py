import random as dt

print('welcome to a rock paper scissors game')
user_choice=input('choose either rock, paper or scissor  ').lower()

if user_choice=='rock' or user_choice=='paper' or user_choice=='scissor':


    choose_from=['rock','paper','scissors']
    computer_choice=dt.choice(choose_from)

    if computer_choice=='rock' and user_choice=='paper':
        print('computer wins')
    elif computer_choice=='scissor' and user_choice=='paper':
        print('computer wins')
    elif computer_choice=='rock' and user_choice=='scissor':
        print('computer wins')
    elif computer_choice==user_choice:
        print('its a tie')
    else:
        print('you win')

else:

    print('you entered an invalid option check spelling or grammar thus you lose')