gifts_list = input().split()
command = input()
while not command == 'No Money':
    data = command.split()
    current_command = data[0]
    gift = data[1]
    if current_command == 'OutOfStock':
        if gift in gifts_list:
            gifts_list = list(map(lambda x: x.replace(gift, 'None'), gifts_list))
    elif current_command == 'Required':
        index = int(data[2])
        if 0 <= index < len(gifts_list):
            gifts_list.pop(index)
            gifts_list.insert(index, gift)
    elif current_command == 'JustInCase':
        gifts_list.pop()
        gifts_list.append(gift)
    command = input()
gifts_list = [i for i in gifts_list if not i == 'None']
print(' '.join(gifts_list))
