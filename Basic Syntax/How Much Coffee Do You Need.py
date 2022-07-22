command = input()
counter = 0
while not command == 'END':
    task = command
    if task in ('coding', 'dog', 'movie', 'cat', 'DOG', 'CAT', 'MOVIE', 'CODING'):
        if task.isupper():
            counter += 2
        elif task.islower():
            counter += 1
    command = input()
if counter <= 5:
    print(counter)
else:
    print('You need extra sleep')
