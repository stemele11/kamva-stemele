




import random


celebrity_data=[
    {
        'name':'neyma',
        'followers':4500005789900,
        'profession':'footballer',
        'country':'united states',
    },
    {
        'name':'rihana',
        'followers':10000000,
        'profession':'singer & business owner',
        'country':'united states',
    },
    {
        'name':'beyonce',
        'followers':254000000,
        'profession':'RNB artist & singer',
        'country':'united states',
    },
    {
        'name':'chloe kardashian',
        'followers':2000000000,
        'profession':'model',
        'country':'united states',
    },
    {
        'name':'Ariana Grande',
        'followers':180000000000,
        'profession':'singer',
        'country':'united states florida',
    },

]

#function to format data
def format_data(account):
    return f'{account['name']} a {account['profession']} from {account['followers']}'

#generate 2 random accounts selection from celebrity data
def random_account(data):
    account=random.choice(data)
    return account


account_a=random_account(celebrity_data)
account_b=random_account(celebrity_data)
if account_b==account_a:
    account_b=random_account(celebrity_data)





#take guess from user
print('WELCOME TO HIGH OR LOW')
print(f'Compare A : {format_data(account_a)}')
print('VS')
print(f'Against B : {format_data(account_b)}')
guess=input("Who has more followers 'A' or 'B': ")


#compare guess with random accounts data




