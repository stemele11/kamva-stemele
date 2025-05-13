from itertools import count
import random

again='y'

while again=='y':
    characters=list('qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+ ,.?}{[]":;~`QWERTYUIOPASDFGHJKLZXCVBNM')
    cipher=[]
    cipher2=[]
    de_message=[]
    to_do=input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()
    shift=int(input('by how many characters you want to shift : '))
    layers=int(input('how many layers of encryption : '))

    def cipher_gen(to_do,shift,layers):
        characters_len=len(characters)
        if to_do=='encrypt':
            count=0
            message=list(input('type message here : '))
            for i in range(len(message)):
                count+=1
                for x in range(characters_len):
                    if message[i]==characters[x]:
                        pos=x+shift*layers
                        cipher.append(characters[pos+count])


            ul=''
            for u in cipher:
                ul+=u
            print(ul)



        elif to_do=='decrypt':
            count=0
            hash_value=list(input('enter there hash value : '))
            for i in range(len(hash_value)):
                count+=1
                for x in range(characters_len):
                    if hash_value[i]==characters[x]:
                        pos1=x-shift*layers
                        de_message.append(characters[pos1-count])
            de_messaged=''
            for m in de_message:
                de_messaged+=m


            print(de_messaged)
    cipher_gen(to_do,shift,layers)
    again=input('do you want to go again press y for yes and n for no ').lower()






