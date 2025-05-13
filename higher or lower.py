
import random


celebrity_followers=[
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





#score to keep current player score
score=0



passed=[]
xlen=len('Between "{celeb1[\'name\']}" from {celeb1[\'country\']} who is a {celeb1[\'profession\']} and "{celeb2[\'name\']}" from {celeb2[\'country\']} who is a {celeb2[\'profession\']} who has more followers on Instagram')
celeb1=random.choice(celebrity_followers)

for celebrity in celebrity_followers:

    if celebrity not in passed:
        pass
    else:
        continue
    celeb2=random.choice(celebrity_followers)

    if celeb2==celeb1 or celeb2 in passed:
        continue
    else:
        pass


    rating=int(input(f'''\n\n Between "{celeb1['name']}" from {celeb1['country']} who is a {celeb1['profession']} and "{celeb2['name']}" from {celeb2['country']} who is a {celeb2['profession']} who has more followers on Instagram
{'*'*xlen}
enter 1 for "{celeb1['name']}" else 2 for"{celeb2['name']}" 
 '''))

    if rating==1:
        if celeb1['followers']>celeb2['followers']:
            score+=1
            print(f'\nyou got it right  {celeb1['name']} : {celeb1['followers']} vs  {celeb2['name']} : {celeb2['followers']} \n')
            print(f'your current score is {score}')
            continue
        else:

            print(f'you lost with a score of {score}')
            print(f'\nyou got it wrong  {celeb1['name']} : {celeb1['followers']} vs  {celeb2['name']} : {celeb2['followers']} \n')
            break
    elif rating==2:
        if celeb2['followers']>celeb1['followers']:
            passed.append(celeb2)
            score+=1
            print(f'\nyou got it right  {celeb2['name']} : {celeb2['followers']} vs  {celeb1['name']} : {celeb1['followers']} \n')
            print(f'your current score is {score}')
            if score>=1:
                celeb1=celeb2
            continue
        else:
            print(f'you lost with a score of {score}')
            print(f'\nyou got it wrong  {celeb2['name']} : {celeb2['followers']} vs  {celeb1['name']} : {celeb1['followers']} \n')
            break
    else:
        print('invalid type input of rating --> enter either 1 or 2 --> nothing else ')
        break





