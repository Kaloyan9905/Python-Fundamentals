data = [i for i in input().split()]
command = input()
counter = 0
while command != 'end':
    valid_index1 = False
    valid_index2 = False
    info = command.split()
    index1 = int(info[0])
    index2 = int(info[1])
    counter += 1
    if 0 <= index1 < len(data):
        valid_index1 = True
    if 0 <= index2 < len(data):
        valid_index2 = True
    if (not valid_index1 or not valid_index2) or index1 == index2:
        half = len(data) // 2
        data.insert(half, f"-{counter}a")
        data.insert(half, f"-{counter}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if data[index1] == data[index2]:
            removed = data[index1]
            data.remove(removed)
            data.remove(removed)
            print(f"Congrats! You have found matching elements - {removed}!")
        else:
            print("Try again!")
    if len(data) == 0:
        print(f"You have won in {counter} turns!")
        exit()
    command = input()
if len(data) != 0:
    print("Sorry you lose :(")
    print(*data, sep=' ')

