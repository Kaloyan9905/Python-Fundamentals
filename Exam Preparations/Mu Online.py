health = 100
bitcoin = 0
dungeon = input().split('|')
room = 0
diff = 0
for current_dungeon in dungeon:
    dungeon_info = current_dungeon.split()
    command = dungeon_info[0]
    number = int(dungeon_info[1])
    room += 1
    if command == 'potion':
        if health < 100:
            health += number
            if health > 100:
                diff = health - 100
                health -= diff
                print(f"You healed for {number - diff} hp.")
            else:
                print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            break
if health <= 0:
    print(f"Best room: {room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")