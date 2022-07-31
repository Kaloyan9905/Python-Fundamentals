n = int(input())
my_dict = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in my_dict:
        my_dict[plant] = {"rarity": rarity, "rating": []}
    else:
        my_dict[plant]["rarity"] += rarity
while True:
    command = input()
    if command == "Exhibition":
        print("Plants for the exhibition:")
        for key, value in my_dict.items():
            if len(value["rating"]) > 0:
                average = sum(value["rating"]) / len(value["rating"])
            else:
                average = 0
            print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")
        break
    else:
        current_command = command.split(": ")
        if current_command[0] == "Rate":
            current_plant, rating = current_command[1].split(" - ")
            rating = int(rating)
            if current_plant in my_dict:
                my_dict[current_plant]["rating"].append(rating)
            else:
                print("error")
        elif current_command[0] == "Update":
            current_plant, new_rarity = current_command[1].split(" - ")
            if current_plant in my_dict:
                my_dict[current_plant]["rarity"] = new_rarity
            else:
                print("error")
        elif current_command[0] == "Reset":
            current_plant = current_command[1]
            if current_plant in my_dict:
                my_dict[current_plant]["rating"].clear()
            else:
                print("error")
