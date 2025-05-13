from word_list import words
import random




print('WELCOME TO HANGMAN')



word=list(random.choice(words))
print(word)



asword=[]
for i in word:
    asword.append('_')

wrong=0
while asword!=word:
    print(asword)

    guessed =input('guess a character  :   ')

    if guessed not in word:
        print(f'{guessed} is not in the word')
        wrong+=1
    if guessed in asword:
        print(f'{guessed} you already guessed')

    if wrong==len(word):
        print('failed')
        break
    print(len(word))
    for i in range(len(word)):

        if guessed==word[i]:
                asword[i]=guessed


        elif guessed not in word:

            if asword[i]=='_':
                continue



finals=''
for letter in word:
    finals+=letter

print(finals)



