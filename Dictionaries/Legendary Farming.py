my_dict = {}
while True:
    valid = False
    data = input().split()
    for index in range(0, len(data), 2):
        key = data[index + 1].lower()
        value = int(data[index])
        if key not in my_dict:
            my_dict[key] = value
        else:
            my_dict[key] += value
        if 'shards' in my_dict:
            if my_dict["shards"] >= 250:
                print('Shadowmourne obtained!')
                my_dict['shards'] -= 250
                valid = True
                break
        if 'fragments' in my_dict:
            if my_dict["fragments"] >= 250:
                print('Valanyr obtained!')
                my_dict['fragments'] -= 250
                valid = True
                break
        if 'motes' in my_dict:
            if my_dict["motes"] >= 250:
                print('Dragonwrath obtained!')
                my_dict['motes'] -= 250
                valid = True
                break
    if valid:
        break
if 'shards' in my_dict:
    print(f"shards: {my_dict['shards']}")
else:
    print('shards: 0')
if 'fragments' in my_dict:
    print(f"fragments: {my_dict['fragments']}")
else:
    print('fragments: 0')
if 'motes' in my_dict:
    print(f"motes: {my_dict['motes']}")
else:
    print('motes: 0')
for key, value in my_dict.items():
    if key not in ('motes', 'fragments', 'shards'):
        print(f"{key}: {value}")