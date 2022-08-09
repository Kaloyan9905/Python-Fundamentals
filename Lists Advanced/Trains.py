n = int(input())
list_empty = [0] * n
command = input()
while command != 'End':
    data = command.split()
    if data[0] == 'add':
        list_empty[-1] += int(data[1])
    elif data[0] == 'insert':
        list_empty[int(data[1])] += int(data[2])
    elif data[0] == 'leave':
        list_empty[int(data[1])] -= int(data[2])
    command = input()
print(list_empty)
