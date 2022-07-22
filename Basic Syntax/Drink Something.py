age = int(input())
drink = ''
if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age <= 21:
    drink = 'beer'
elif age > 21:
    drink = 'whisky'
print(f'drink {drink}')
