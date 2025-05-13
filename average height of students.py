student_heights=input('enter student heights separated by a comma     ').split(',')
print(student_heights)

sum=0
count=0
for height in student_heights:
    sum+=( float(height))
    count +=1

avg=sum/count

print(f'average height of students is {round(avg,1)}m')

