name = 'eric Pearson'

# Упражнение 3.
message = f'Hello {name}, would you like to learn some Python today?'
print(message)

# Упражнение 4.
message = f'Hello {name.lower()}, would you like to learn some Python today?'
print(message)
message = f'Hello {name.upper()}, would you like to learn some Python today?'
print(message)
message = f'Hello {name.title()}, would you like to learn some Python today?'
print(message)

# Упражнение 5.
message = f'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message)

# Упражнение 6.
famous_person = 'Albert Einstein'

message = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."'
print(message)

# Упражнение 7.
famous_person = ' \t\nAlbert Einstein \t\n'

print(f'|{famous_person} once said, "A person who never made a mistake never tried anything new."|')
print(f'|{famous_person.lstrip()} once said, "A person who never made a mistake never tried anything new."|')
print(f'|{famous_person.rstrip()} once said, "A person who never made a mistake never tried anything new."|')
print(f'|{famous_person.strip()} once said, "A person who never made a mistake never tried anything new."|')
