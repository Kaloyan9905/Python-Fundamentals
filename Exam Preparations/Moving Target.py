input_line = [int(i) for i in input().split()]
command = input()
while not command == 'End':
    command = command.split()
    if command[0] == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(input_line):
            input_line[index] -= power
            if input_line[index] <= 0:
                input_line.pop(index)
    elif command[0] == 'Add':
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(input_line):
            input_line.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        if 0 <= index < len(input_line):
            before_radius = index - radius
            after_radius = index + radius
            if after_radius in range(len(input_line)) and before_radius in range(len(input_line)):
                input_line = input_line[0:before_radius] + input_line[after_radius + 1::]
            else:
                print('Strike missed!')
    command = input()
result = '|'.join(str(x) for x in input_line)
print(result)
