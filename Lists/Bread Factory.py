data = input().split('|')
coins = 100
energy = 100
gained = 0
event_handle = True
for current_command in data:
    info = current_command.split('-')
    event = info[0]
    number = int(info[1])
    if event == 'rest':
        temp_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained = energy - temp_energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
            continue
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            event_handle = False
            break
if event_handle:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")