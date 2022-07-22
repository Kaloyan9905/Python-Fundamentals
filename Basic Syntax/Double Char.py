string = input()
while not string == 'End':
    if string == 'SoftUni':
        string = input()
    for i in string:
        final = i * 2
        print(f'{final}', end='')
    print()
    string = input()




