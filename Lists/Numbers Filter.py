n = int(input())
numbers = list()

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered = list()

if command == 'even':
    for current_number in numbers:
        if current_number % 2 == 0:
            filtered.append(current_number)
elif command == 'odd':
    for current_number in numbers:
        if current_number % 2 != 0:
            filtered.append(current_number)
elif command == 'positive':
    for current_number in numbers:
        if current_number >= 0:
            filtered.append(current_number)
elif command == 'negative':
    for current_number in numbers:
        if current_number < 0:
            filtered.append(current_number)
print(filtered)
