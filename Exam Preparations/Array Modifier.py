array = [int(i) for i in input().split()]
command = input()
while command != 'end':
    info = command.split()
    current_operation = info[0]
    if current_operation == 'swap':
        index1 = int(info[1])
        index2 = int(info[2])
        array[index1], array[index2] = array[index2], array[index1]
    elif current_operation == 'multiply':
        index1 = int(info[1])
        index2 = int(info[2])
        answer = int(array[index1]) * int(array[index2])
        array.pop(index1)
        array.insert(index1, answer)
    elif current_operation == 'decrease':
        array = [int(i) - 1 for i in array]
    command = input()
print(*array, sep=', ')
