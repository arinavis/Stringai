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





