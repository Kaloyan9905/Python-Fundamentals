data = input().split(', ')
valid_list = []
for word in data:
    counter = 0
    if 3 <= len(word) <= 16:
        for char in word:
            if char.isdigit():
                counter += 1
            elif char.isalpha():
                counter += 1
            elif char == '-':
                counter += 1
            elif char == '_':
                counter += 1
            else:
                break
        if counter == len(word):
            valid_list.append(word)

for word in valid_list:
    print(word)

