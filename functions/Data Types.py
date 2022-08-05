def answer():
    res = 0
    if command == 'int':
        res = int(command2) * 2
        return print(f'{res}')
    elif command == 'real':
        res = float(command2) * 1.5
        return print(f'{res:.2f}')
    elif command == 'string':
        return print(f'${command2}$')


command = input()
command2 = input()
answer()
