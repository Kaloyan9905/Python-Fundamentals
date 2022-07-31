my_dict = {}
command = input()
while command != "Sail":
    city, population, gold = command.split("||")
    population, gold = int(population), int(gold)
    if city not in my_dict:
        my_dict[city] = {"population": population, "gold": gold}
    else:
        my_dict[city]["population"] += population
        my_dict[city]["gold"] += gold
    command = input()
event = input()
while event != "End":
    event = event.split("=>")
    if event[0] == "Plunder":
        town, people, gold = event[1], int(event[2]), int(event[3])
        my_dict[town]["gold"] -= gold
        my_dict[town]["population"] -= people
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if my_dict[town]["gold"] == 0 or my_dict[town]["population"] == 0:
            print(f"{town} has been wiped off the map!")
            del my_dict[town]
    elif event[0] == "Prosper":
        town, gold = event[1], int(event[2])
        if gold > 0:
            my_dict[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {my_dict[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
    event = input()
if len(my_dict) > 0:
    print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")
    for key, value in my_dict.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
