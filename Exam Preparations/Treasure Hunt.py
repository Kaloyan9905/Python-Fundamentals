chest = [i for i in input().split('|')]
removed_items = []
while True:
    command = input().split()

    loot = []

    if command[0] == "Yohoho!":
        break
    if command[0] == "Loot":
        loot = [item for item in command if item not in chest]
        for i in loot:
            if i != 'Loot':
                chest.insert(0, i)
    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(chest):
            item_to_add = chest[index]
            chest.pop(index)
            chest.append(item_to_add)
    elif command[0] == "Steal":
        count = int(command[1])
        if count >= len(chest):
            removed_items = chest
            print(*removed_items, sep=', ')
            print("Failed treasure hunt.")
            exit()
        else:
            start = len(chest) - count
            removed_items = chest[start::]
            del chest[start::]
            print(*removed_items, sep=', ')
if len(chest) > 0:
    sum_len = 0
    for i in chest:
        sum_len += len(i)
    average_treasure_gain = f"{sum_len / len(chest):.2f}"
    print(f"Average treasure gain: {average_treasure_gain} pirate credits.")
