print('Welcome to the tip calculator')
print(30*'*')

total_bill=float(input('what was the total bill ? $'))
tip=float(input('what percentage tip you\'d like to give ? '))
number_of_people=int(input('how many number of people is the bill being split'))
#calculates bill with tip and divide by number of people
each_pay=(total_bill+((tip/100)*total_bill))/number_of_people
#displays amount each person should pay and round it to 2 decimal places
print(f'each person should pay ${each_pay:.2f}')