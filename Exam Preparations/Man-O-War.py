pirate_ships = [int(i) for i in input().split('>')]
warships = [int(i) for i in input().split('>')]
health_per_ship = int(input())
command = input()
total_pirate_sum = 0
total_warship_sum = 0
while not command == 'Retire':
    info = command.split()
    if info[0] == 'Fire':
        index = int(info[1])
        damage = int(info[2])
        if 0 <= index < len(warships):
            warships[index] -= damage
            if warships[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif info[0] == 'Defend':
        start = int(info[1])
        end = int(info[2])
        damage = int(info[3])
        if 0 <= start < len(pirate_ships):
            if 0 <= end < len(pirate_ships):
                for i in pirate_ships:
                    pirate_ships[start] -= damage
                    start += 1
                    if start == end + 1:
                        break
                for i in pirate_ships:
                    if i <= 0:
                        print("You lost! The pirate ship has sunken.")
                        exit()
    elif info[0] == 'Repair':
        index = int(info[1])
        health_to_add = int(info[2])
        if 0 <= index < len(pirate_ships):
            pirate_ships[index] += health_to_add
            if health_to_add > health_per_ship:
                pirate_ships[index] = health_per_ship
    elif info[0] == 'Status':
        twenty_percent = health_per_ship * 0.20
        pirate_ship_list = [i for i in pirate_ships if i < twenty_percent]
        pirate_ship_count = len(pirate_ship_list)
        print(f"{pirate_ship_count} sections need repair.")
    command = input()
valid = True
for i in pirate_ships:
    if i == 0:
        valid = False
for i in warships:
    if i == 0:
        valid = False
if valid:
    for i in pirate_ships:
        total_pirate_sum += int(i)
    for i in warships:
        total_warship_sum += int(i)
    print(f"Pirate ship status: {total_pirate_sum}")
    print(f'Warship status: {total_warship_sum}')
