numbers = [int(i) for i in input().split()]
command = input()
counter = 0
new_list = []
while not command == 'End':
    index = int(command)
    if 0 <= index < len(numbers):
        if not numbers[index] == -1:
            value = numbers[index]
            numbers[index] = -1
        for i in numbers:
            if i != -1:
                if i > value:
                    i -= value
                    new_list.append(i)
                else:
                    i += value
                    new_list.append(i)
            else:
                new_list.append(-1)
        numbers = new_list
        new_list = []
    command = input()
for i in numbers:
    if i == -1:
        counter += 1

print(f"Shot targets: {counter} ->", end=' ')
for i in numbers:
    print(i, end=' ')
