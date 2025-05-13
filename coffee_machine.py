from platform import machine
from files import  coins,coin_insert,coffee_type,machine_coffee_resources
print('WELCOME TO COFFEE MACHINE')
coffee_choice=input(' what would you like ? (espresso/latte/cappuccino): ').lower().title()


print('\n\nplease insert coins.....')
for coin in coin_insert:
    coin_insert[coin]=input(f'how many {coin} ')

def resources():
    print(f'''\n\ncurrent coffee making resources
    {'*'*50} 
    water : {machine_coffee_resources['water']}ml
    coffee : {machine_coffee_resources['coffee']}g
    milk : {machine_coffee_resources['milk']}ml
    'money': ${machine_coffee_resources['money']}''')
resources()

def inserted(coin_insert):
    total=0
    for coin in coin_insert:
        total+=float(coins[coin])*float(coin_insert[coin])
    return round(total,2)

total=inserted(coin_insert)



coffee_list=[]
for i in coffee_type:
    coffee_list.append(i)

print(total)
money_add=[]
def change_back(coffe_choice):
    value=0
    for coffee in coffee_list:

        for keys in coffee.keys():
            if keys==coffee_choice:
                if float(total)>coffee[keys]['price']:
                    value=total-float(coffee[keys]['price'])
                    money_add.append(total-value)
                    return value


change_back(coffee_choice)

def money():
    machine_coffee_resources['money']=sum(money_add)
    if machine_coffee_resources['money']>0:
        print(f'\nhere is you {coffee_choice} ☕️ enjoy')
        print(f'\nhere is ${change_back(coffee_choice)} in change')

    else:
        return 'no coins received bye'
money()

depleted=[]
def order(coffee_choice):
    for coffeet in coffee_list:
        for keys in coffeet.keys():
            if coffee_choice==keys:

                if machine_coffee_resources['water']>=coffeet[keys]['water']:
                    machine_coffee_resources['water']-=coffeet[keys]['water']
                elif machine_coffee_resources['water']<coffeet[keys]['water']:
                    print(machine_coffee_resources['water'])
                    print(coffeet[keys]['water'])
                    depleted.append('water')
                if machine_coffee_resources['coffee']>=coffeet[keys]['coffee']:
                    machine_coffee_resources['coffee']-=coffeet[keys]['coffee']
                elif machine_coffee_resources['coffee']<coffeet[keys]['coffee']:
                    depleted.append('coffee')
                if machine_coffee_resources['milk']>=coffeet[keys]['milk']:
                    machine_coffee_resources['milk']-=coffeet[keys]['milk']
                elif machine_coffee_resources['milk']<coffeet[keys]['milk']:
                    depleted.append('milk')



order(coffee_choice)

resources()
again=input(f'do you want to oder again ? y/n ')

while again=='y':
    coffee_choice=input(' what would you like ? (espresso/latte/cappuccino): ').lower().title()

    print('\n\nplease insert coins.....')
    for coin in coin_insert:
        coin_insert[coin]=input(f'how many {coin} ')

    inserted(coin_insert)


    money()
    change_back(coffee_choice)
    if len(depleted)!=0:
        print(f'Here is your refund ${total}')
        print(f'not enough {depleted}')
        break
    else:
        order(coffee_choice)
        machine_coffee_resources['money']+=total-change_back(coffee_choice)




    if machine_coffee_resources['money']>0:
        print(f'\nhere is you {coffee_choice} ☕️ enjoy')
    print(f'\nhere is ${change_back(coffee_choice)} in change')
    resources()
    again=input(f'do you want to oder again ? y/n ')
    if again=='n':
        break
    else:
        continue










