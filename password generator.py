from random import randrange
from shlex import split

print('Welcome to password generator app')
print((27*'*'))

import random as dt
size=int(input('how many characters you want in your password '))+1
num_characters=int(input('how many number you\'d want to be in your password '))
symbol_characters=int(input('how many symbols you\'d like to be in your password' ))
char_size=size-num_characters-symbol_characters

symbols='!@#$%^&*()_+{}[]|?~'
symbols.split(',')
chars='qwertyuiopasdfghjklzxcvbnm'
chars.split(',')
password=[]


for i in range(num_characters):
    password.append(str(dt.randint(0,9)))

for i in range(symbol_characters):
    password.append(dt.choice(symbols))


for i in range(char_size):
    password.append(dt.choice(chars))

new_pass=''
for i in range(0,(size-1)):
    new_pass+=(password[i])

finalpass=''
for i in range(0,(len(new_pass))):
    finalpass+=new_pass[dt.randint(0,len(new_pass)-1)]


print(f'your generated password is : {finalpass} ')




