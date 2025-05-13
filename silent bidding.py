import sys

print('Welcome to secret bidding program')
more_bidders=True
bidders=[]
while more_bidders:
    bidder_name=input('what is your name ? ')
    bid_amount=float(input('how much you bidding ? $'))

    bidder={
        'name':bidder_name,
        'bid':bid_amount
    }
    bidders.append(bidder)
    done=input('are there more people bidding yes or no ? ').lower()
    if done=='no':
        more_bidders=False
highest=0
name=''

x=open('bidders.txt','r+')



for person in bidders:
    if person['bid']>highest:
        highest=person['bid']
        name=person['name']
        x.write(person['name'])
        x.write(str(person['bid']))





f=x.readline()
print(f)
x.close()
print(f'{name} won the bid by bidding ${highest}')










