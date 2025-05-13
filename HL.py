import random
score=0

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
    """format communicated information to the user"""
    return f'{account['name']} a {account['profession']} from {account['country']}'

#generate 2 random accounts selection from celebrity data
def random_account(data):
    """random account generator"""
    account=random.choice(data)
    return account






#take guess from user
def start(account_a,account_b):
    print('WELCOME TO HIGH OR LOW')
    print(f'Compare A : {format_data(account_a)}')
    print('VS')
    print(f'Against B : {format_data(account_b)}')
    return input("Who has more followers 'A' or 'B': ").lower().title()

def followers(account):
    """extract followers from account"""
    return account['followers']

#compare guess with random accounts data
def compare(account_a,account_b,guess):
    """verify if user guess is correct"""
    if followers(account_a)>followers(account_b):
        return guess=='a'
    else:
        account_a=account_b
        return guess=='b'









right=True
for celeb in celebrity_data:
    if right:

        account_a=random_account(celebrity_data)
        account_b=random_account(celebrity_data)
        if account_b==account_a:
            continue
        else:
            pass
        guess=start(account_a,account_b)
        score+=1
        start(account_a,account_b)
        if compare(account_a,account_b,guess):
            print(f'you are right current score is {score}')
        else:
            print(f'got it wrong with a score of {score}')







if right:
    print(f'your final score is {score}')
else:
    print(f'wrong guess, your final score is {score}')


























