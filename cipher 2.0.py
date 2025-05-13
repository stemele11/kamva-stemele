
print('WELCOME TO CAESAR CIPHER')
print('*'*len('WELCOME TO CAESAR CIPHER'))

hash=''
original_message=''
new_position=0
again='yes'


while again=='yes':
    direction=input('type encode to encode and decode to decode your message ').lower()
    shift=int(input('type the shift number '))
    message=input('enter message here ')
    characters=list('qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+,.? }{[]":;~`QWERTYUIOPASDFGHJKLZXCVBNM')

    for letter in message:
            if direction=='encode':
                position=characters.index(letter)
                new_position=position+shift
                if new_position>len(characters):
                    new_position=new_position%len(message)
                hash+=characters[new_position]
                if len(message)==len(hash):
                    print(f'{hash} is the encoded message')
            else:
                if letter in message:
                    current_position=characters.index(letter)

                    if shift>len(characters):
                        shift=current_position
                    original_position=current_position-shift
                    print(original_position)
                    if characters[original_position-1]==' ':
                        original_position+=characters[original_position-1]
                    else:
                        original_message+=characters[original_position]
                    if len(message)==len(original_message):
                        print(f'{original_message} is the original decoded message')
    again=input('you want to go again ? yes or no :  ')








