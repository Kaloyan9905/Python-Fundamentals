n = int(input())
my_dict = {}

for i in range(n):
    name, hit, mana = input().split()
    hit, mana = int(hit), int(mana)
    if hit > 100:
        hit = 100
    if mana > 200:
        mana = 200
    my_dict[name] = {"hit": hit, "mana": mana}

while True:
    command = input()
    if command == "End":
        for key, value in my_dict.items():
            print(key)
            print(f"  HP: {value['hit']}")
            print(f"  MP: {value['mana']}")
        exit()
    else:
        command = command.split(" - ")
        if command[0] == "CastSpell":
            hero, mp_needed, spell = command[1], int(command[2]), command[3]
            mp_needed = int(mp_needed)
            if my_dict[hero]["mana"] >= mp_needed:
                left_mana = my_dict[hero]["mana"] - mp_needed
                my_dict[hero]["mana"] -= mp_needed
                print(f"{hero} has successfully cast {spell} and now has {left_mana} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell}!")
        elif command[0] == "TakeDamage":
            hero, damage, attacker = command[1], int(command[2]), command[3]
            my_dict[hero]["hit"] -= damage
            if my_dict[hero]["hit"] > 0:
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {my_dict[hero]['hit']} HP left!")
            else:
                del my_dict[hero]
                print(f"{hero} has been killed by {attacker}!")
        elif command[0] == "Recharge":
            hero, amount = command[1], int(command[2])
            first_mana = my_dict[hero]["mana"]
            my_dict[hero]["mana"] += amount
            if my_dict[hero]["mana"] > 200:
                my_dict[hero]["mana"] = 200
                print(f"{hero} recharged for {200 - first_mana} MP!")
            else:
                print(f"{hero} recharged for {amount} MP!")
        elif command[0] == "Heal":
            hero, amount = command[1], int(command[2])
            first_hp = my_dict[hero]["hit"]
            my_dict[hero]["hit"] += amount
            if my_dict[hero]["hit"] > 100:
                my_dict[hero]["hit"] = 100
                print(f"{hero} healed for {100 - first_hp} HP!")
            else:
                print(f"{hero} healed for {amount} HP!")
