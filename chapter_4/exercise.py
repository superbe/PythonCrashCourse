# Упражнение 1.

pizza = ['Margarita', 'pepperoni', 'americana']

for name in pizza:
    print(f'I like {name.lower()} pizza.')

print('I really love pizza!')

# Упражнение 2.
pets = ['dog', 'cat', 'parrot', 'hamster']

for pet in pets:
    print(f'A {pet} would make a great pet')

print('Any of these animals would make a great pet!')

# Упражнение 3.
for i in range(1, 21):
    print(i)

# Упражнение 4.
million = range(1, 1_000_001)
for i in million:
    print(i)

# Упражнение 5.
million = range(1, 1_000_001)
print(min(million))
print(max(million))
print(sum(million))

# Упражнение 6.
odd = range(1, 21, 2)
for i in odd:
    print(i)

# Упражнение 7.
triples = range(3, 31, 3)
for i in triples:
    print(i)

# Упражнение 8.
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)

for i in cubes:
    print(i)

# Упражнение 9.
cubes = [i ** 3 for i in range(1, 11)]

for i in cubes:
    print(i)

# Упражнение 10.
pets = ['dog', 'cat', 'parrot', 'hamster', 'pony', 'pig']
print(pets)

print('The first three items in the list are:')
print(pets[:3])

print('Three items from the middle of the list are:')
print(pets[2:5])

print('The last three items in the list are:')
print(pets[-3:])

# Упражнение 11.
pizza = ['Margarita', 'Sicilian', 'Diabola', 'Four cheeses', 'Seafood', 'Neapolitan']
friend_pizzas = pizza[:]

pizza.append('Calzone')
friend_pizzas.append('Capricciosa')

print('My favorite pizzas are:')
for item in pizza:
    print(item)

print('My friend’s favorite pizzas are:')
for item in friend_pizzas:
    print(item)

# Упражнение 12.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for item in my_foods:
    print(item)
print("\nMy friend's favorite foods are:")
for item in friend_foods:
    print(item)

# Упражнение 13.
buffet = ('salad', 'borscht', 'porridge', 'lamb', 'compote')
for item in buffet:
    print(item)

# buffet[-1] = 'tea'
print(buffet)

buffet = ('salad', 'borscht', 'porridge', 'lamb', 'tea')
print(buffet)
