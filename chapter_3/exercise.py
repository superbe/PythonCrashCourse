# Упражнение 1.
friends = ['Alex', 'fred', 'Kate', 'eugene']

print(friends[0])
print(friends[1].title())
print(friends[2])
print(friends[3].title())

# Упражнение 2.
message = f'Hi, {friends[0].title()}!'
print(message)

message = f'Hi, {friends[1].title()}!'
print(message)

message = f'Hi, {friends[2].title()}!'
print(message)

message = f'Hi, {friends[3].title()}!'
print(message)

# Упражнение 3.
motorcycles = ['Honda', 'Ural', 'Java']

print(f'Я хотел бы купить мотоцикл {motorcycles[-1]}')
print(f'Я хотел бы купить мотоцикл {motorcycles[-2]}')
print(f'Я хотел бы купить мотоцикл {motorcycles[-3]}')

# Упражнение 4.
guests = ['Albert', 'John', 'Elton']

print(f'Dear {guests[0].title()}, I invite you to visit.')
print(f'Dear {guests[1].title()}, I invite you to visit.')
print(f'Dear {guests[2].title()}, I invite you to visit.')

# Упражнение 5.
busy_guest = 'Albert'
print(f'{busy_guest.title()} is busy and will not be able to come.')

guests[0] = 'Eugene'

print(f'Dear {guests[0].title()}, I invite you to visit.')
print(f'Dear {guests[1].title()}, I invite you to visit.')
print(f'Dear {guests[2].title()}, I invite you to visit.')

# Упражнение 6.
print('Number of guests increased.')
guests.insert(0, 'Nikolay')
guests.insert(2, 'Peter')
guests.append('Alex')

print(f'Dear {guests[0].title()}, I invite you to visit.')
print(f'Dear {guests[1].title()}, I invite you to visit.')
print(f'Dear {guests[2].title()}, I invite you to visit.')
print(f'Dear {guests[3].title()}, I invite you to visit.')
print(f'Dear {guests[4].title()}, I invite you to visit.')
print(f'Dear {guests[5].title()}, I invite you to visit.')

# Упражнение 7.
print('Only two guests are invited to dinner.')

name = guests.pop()
print(f'Dear {name.title()}, I am sorry, but your invitation is canceled.')
name = guests.pop()
print(f'Dear {name.title()}, I am sorry, but your invitation is canceled.')
name = guests.pop()
print(f'Dear {name.title()}, I am sorry, but your invitation is canceled.')
name = guests.pop()
print(f'Dear {name.title()}, I am sorry, but your invitation is canceled.')

print(f'Dear {guests[0].title()}, the invitation remains valid.')
print(f'Dear {guests[1].title()}, the invitation remains valid.')

del guests[0]
del guests[0]

print(guests)

# Упражнение 8.
countries = ['Greece', 'France', 'Algeria', 'Pakistan', 'Iran']

print(countries)
print(sorted(countries))
print(countries)

print(sorted(countries, reverse=True))
print(countries)

countries.reverse()
print(countries)

countries.reverse()
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

# Упражнение 9.
guests = ['Albert', 'John', 'Elton']
print(len(guests))

# Упражнение 10.
colors = ['Кадмий лимонный', 'Кадмий желтый средний', 'Охра желтая', 'Сиена натуральная', 'Золотистая',
          'Кадмий оранжевый', 'Охра красная', 'Сиена жженая', 'Железоокисная светло-красная', 'Алая',
          'Краплак красный светлый', 'Карминовая', 'Фиолетовая', 'Ультрамарин', 'Кобальт синий', 'Голубая',
          'Желто-зеленая', 'Изумрудно-зеленая', 'Зеленая', 'Умбра', 'Марс коричневый', 'Умбра жженая', 'Сепия',
          'Нейтрально-черная']
print(colors)

print(colors[0])
print(colors[-1])

colors.append('Церулеум')
print(colors)
colors.insert(0, 'Немецкая голубая')
print(colors)
colors.insert(5, 'Берлинская черная')
print(colors)
del colors[5]
print(colors)
color = colors.pop()
print(colors)
print(color)
colors.remove('Немецкая голубая')
print(colors)
print(sorted(colors))
print(colors)
print(sorted(colors, reverse=True))
print(colors)
colors.reverse()
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
print(len(colors))

# Упражнение 10.
print(colors[24])
