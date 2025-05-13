travel_log={
    'province':{'eastern cape':{'cities':['qgeberha','east london','king williams town','mthatha'],'costs':10500},
                'gauteng':{'cities':['soweto','thabatshwane','gugulethu','gauteng east'],'costs':8500},
                'western cape':{'cities':['khayelitsha','somerset east','somerset west','extension v2'],'costs':17000},
}
}

print(f'''cities visited in eastern cape provide\n {'*'*34} \n{travel_log['province']['eastern cape']['cities']}''')
print(f'''Total cost of visiting {travel_log['province']['eastern cape']['cities']} : \nTotal == ${travel_log['province']['eastern cape']['costs']}''')


travel_logs=[
    {
        'country':'france',
        'visits':'12',
        'cities':['paris','lille','dijon']
    },
    {
        'country':'germany',
        'visits':5,
        'cities':['berlin','hamburg','stuttgart']
    }
]

done=True
country=input('name of country you visited : ')
period=int(input('how many days of visit : '))
cities=[]
while done:
 visited_city=input('enter a city you visited : ')
 finsh=input('want to add another city you visited ? yes or no ')
 cities.append(visited_city)
 if finsh=='no':
     done=False

add_country={}
towns=[]

def new_country_add(new_country,num_of_visits,city=[]):
    add_country['country']=new_country
    add_country['visits']=num_of_visits

    add_country['cities']=city
    travel_logs.append(add_country)


new_country_add(country,period,cities)







new_country={'country':'Russia','visits':7,'cities':['moscow','saint peterson','alvory']}
travel_logs.append(new_country)
print(travel_logs)


