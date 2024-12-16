# write a list of names

names = ['John', 'Paul', 'George', 'Ringo']

# write a for loop to print each name in the list
for index, name in enumerate(names):
    print(name)
    if (names[index] == 'George'):
        print("George is a Beatle")
    break


# write a tuple of cities
cities = ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')

# write a for loop to print each city in the tuple
for index, city in enumerate(cities):
    print(city)
    if (cities[index] == 'Chicago'):
        print("Chicago is a great city")
    break
