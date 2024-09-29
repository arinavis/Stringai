import re
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
first_latters = name1[0] + surname1[0]
print(first_latters)

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
