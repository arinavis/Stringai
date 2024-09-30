import re
import random
import string
# 1 uzd
aktoriai = ['Johny Depp', 'Jensen Ackles']
trump_str = min(aktoriai, key=len)
print('Trumpesnis vardas yra: ', trump_str)

name = "Johny"
surname = "depp"

if len(name) > len(surname):
    print(surname)
else:
    print(name)

# 2 uzd.

vardas = 'Leonardo'
pavarde = 'Dicaprio'

print(vardas.upper(), pavarde.lower())

# 3 uzd
name1 = 'Angelina'
surname1 = 'Jolie'
first_letters = name1[0] + surname1[0]
print(first_letters)

# 4 uzd
actorName = 'Brad'
actorSurname = 'Pitt'
short_name = actorName[-3:] + actorSurname[-3:]
print(short_name)

# kaip veikia?

# 5 uzd
filmo_pav = 'An American in Paris'
changes = filmo_pav.replace('a','*').replace('A', '*')
print(changes)

# 6 uzd.
old_name = 'An American in Paris'
new_name = re.sub('[AaĄąEeĖėIiĮįYyOoUuŲųŪū]', '', old_name)
print(new_name)

old_name1 = "Breakfast at Tiffany's"
new_name1 = re.sub('[AaĄąEeĖėIiĮįYyOoUuŲųŪū]', '', old_name1)
print(new_name1)

old_name2 = "2001: A Space Odyssey"
new_name2 = re.sub('[AaĄąEeĖėIiĮįYyOoUuŲųŪū]', '', old_name2)
print(new_name2)

old_name3 = "It's a Wonderful Life"
new_name3 = re.sub('[AaĄąEeĖėIiĮįYyOoUuŲųŪū]', '', old_name3)
print(new_name3)

# 7 uzd
starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)

result = re.search(r'\d', starWars)
print(result.group())

print(starWars[-14:-13])
print(re.sub(r"\D+","", starWars))

# 8 uzd.

fraze = "Don't Be a Menace to South Central While Drinking Your Juice in the Hoo"


# 9 uzd.
raides1 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
raides2 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
raides3 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

print(raides1 + raides2 + raides3)

random_string = ''.join(random.sample(string.ascii_lowercase, 3))
print(random_string)