n = int(input())
for i in range(n):
    command = input()
    if '_' in command:
        print(f"{command} is not pure!")
    elif '.' in command:
        print(f"{command} is not pure!")
    elif ',' in command:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")