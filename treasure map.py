

row1=['1😍','4😍','7😍']
row2=['2❤️','5❤️','8❤️']
row3=['3⚽️️','6⚽️','9⚽️️']

map=[row1,row2,row3]

print(f'{row1}\n{row2}\n{row3}')


row=int(input('enter row you want to access by number '))
column=int(input('enter column you want to access by number '))

#making it user friendly by allowing user to give input starting from 1 but minus 1 in the pragram
if column>0:
    column-=1
if row>0 :

    row-=1
    #replace located spot with an X
    map[row][column]='X'
    print(f'{row1}\n{row2}\n{row3}')
    print(map[row][column])
else:
    map[row][column]='X'
    print(f'{row1}\n{row2}\n{row3}')
    print(map[row][column])