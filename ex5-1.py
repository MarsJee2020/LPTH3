
name = 'Mars Jee'
age = 47
hobbies = ['Sport', 'Karate', 'Reading']

print(f"Hi~ I'm {name}, it's nice to meet you")
print(f'I am {age} years old.')

print(f"my hobbies ares {hobbies}")
print('I can list down my hobbies per line')

for item in hobbies:
    print(item)

print('Or I can print out them in one line, separated by a special string')

for item in hobbies:
    print(item, end='<-->')

