import random

print('WELCOME TO THE BLACKJACK PROGRAM')
cards={
    'jack':10,
    'queen':10,
    'king':10,
    '10':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2,
    'ace1':1,
    'ace11':11,



}


cards_list=['jack','queen','king','10','9','8','7','6','5','4','3','2','ace1','ace11']



computer=[]
user=[]
user_cards=0
computer_cards=0

for card in cards:
    key_user=random.choice(cards_list)
    key_computer=random.choice(cards_list)
    key=random.choice(cards_list)
    user_cards+=int(cards[key_user])
    user.append(int(cards[key_user]))
    computer_cards+=int(cards[key_computer])
    computer.append(int(cards[key_computer]))
    print(f'current score for you is {user_cards} your cards are {user}')
    print(f'current score for dealer is {computer_cards} and current cards are {computer}')
    if len(computer)==2 and computer_cards<17:
        computer_cards+=int(cards[key])
        computer.append(int(cards[key]))


    elif computer_cards==21 and len(computer)==2:
        if 11 in computer:

            computer_cards=0

            computer.remove(cards['ace11'])

            computer.append('black jack')

            print('Dealer wins because of black jack')
            break

    elif computer_cards>21:
        if 11 in computer:
            computer_cards-=11
            computer_cards+=1
            computer.remove(cards['ace11'])
            computer.append(cards['ace1'])
            print(computer_cards)
            continue
    if user_cards==21 and len(user)==2:
        if 11 in user:

            user_cards=0

            user.remove(cards['ace11'])

            user.append('black jack')

            print('you win because of black jack')
            break

    elif user_cards>21:
        if 11 in user:
            user_cards-=11
            user_cards+=1
            user.remove(cards['ace11'])
            user.append(cards['ace1'])
            print(user_cards)
            continue


    if user_cards <21 :
        if computer_cards<21:
                get_another_card=input('get another card yes or no ')
                if get_another_card=='no':
                    if user_cards>computer_cards:
                        print('You win')
                        break
                    elif computer_cards>user_cards :
                        if computer_cards<21:
                            print('Dealer wins')
                            break
                    elif computer_cards==user_cards:
                        print('draw')
                        break
                elif get_another_card=='yes':
                    continue

        elif computer_cards>=21:
            print('you win')
            break
        elif computer_cards==user_cards:
            print('draw')
            break


    elif user_cards>=21:

        print('dealer win')
        break
    elif computer_cards==user_cards:
        print('draw')
        break
    elif computer_cards>=21:
        print('you win')
        break














