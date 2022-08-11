collecting_items = input().split(', ')
command = input()
item_inventory = collecting_items
while not command == 'Craft!':
    info = command.split(' - ')
    current_command = info[0]
    item = info[1]
    if current_command == 'Collect':
        if item not in item_inventory:
            item_inventory.append(item)
    elif current_command == 'Drop':
        if item in item_inventory:
            item_inventory.remove(item)
    elif current_command == 'Combine Items':
        new_info = item.split(':')
        new_item = new_info[1]
        old_item = new_info[0]
        if old_item in item_inventory:
            for i in range(len(item_inventory)):
                if item_inventory[i] == old_item:
                    item_inventory.insert(i + 1, new_item)
                    break
    elif current_command == 'Renew':
        if item in item_inventory:
            item_inventory.remove(item)
            item_inventory.append(item)
    command = input()
print(', '.join(item_inventory))
