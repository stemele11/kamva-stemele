scores =input('enter students scores separated by a space ').split()


high_score=0
for score in scores:

    if high_score < int(score):
        high_score=int(score)
print(f'highest score in the class is {high_score}')

li1=[]
for i in range(1,51):
    li1.append(i)
li2=[]
for i in range(51,101):
    li2.append(i)
li2.reverse()

print(li1)
print(li2)
