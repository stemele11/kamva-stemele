number=int(input('enter number you want to use '))
count=0

for i in range(2,number+1,2):
    count+=1

print(f'sum of total of even numbers from 1 to {number} is {count}')