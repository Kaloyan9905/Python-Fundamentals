def new_version():
    first = int(version[0])
    second = int(version[1])
    third = int(version[2]) + 1
    if second >= 9 and third >= 9:
        second = 0
        third = 0
        first += 1
    if third >= 9:
        third = 0
        second += 1
    return print(f'{first}.{second}.{third}')


version = input().split('.')
new_version()
