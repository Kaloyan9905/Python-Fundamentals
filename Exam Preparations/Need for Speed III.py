def drive(current_dict, current_car, current_distance, current_fuel):
    if current_dict[current_car]["fuel"] >= current_fuel:
        current_dict[current_car]["mileage"] += current_distance
        current_dict[current_car]["fuel"] -= current_fuel
        print(f"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if current_dict[current_car]["mileage"] >= 100000:
        print(f"Time to sell the {current_car}!")
        del current_dict[current_car]
    return current_dict


def refuel(current_dict, current_car, current_fuel):
    first_fuel = current_dict[current_car]["fuel"]
    current_dict[current_car]["fuel"] += current_fuel
    if current_dict[current_car]["fuel"] > 75:
        current_dict[current_car]["fuel"] = 75
        print(f"{current_car} refueled with {75 - first_fuel} liters")
    else:
        print(f"{current_car} refueled with {current_fuel} liters")
    return current_dict


def revert(current_dict, current_car, current_kilometers):
    current_dict[current_car]["mileage"] -= current_kilometers
    if current_dict[current_car]["mileage"] > 10000:
        print(f"{current_car} mileage decreased by {current_kilometers} kilometers")
    else:
        current_dict[current_car]["mileage"] = 10000
    return current_dict


n = int(input())
my_dict = {}

for i in range(n):
    car, mileage, fuel = input().split("|")
    mileage, fuel = int(mileage), int(fuel)
    my_dict[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        for key, value in my_dict.items():
            print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
        exit()
    command = command.split(" : ")
    if command[0] == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        my_dict = drive(my_dict, car, distance, fuel)
    elif command[0] == "Refuel":
        car, fuel = command[1], int(command[2])
        my_dict = refuel(my_dict, car, fuel)
    elif command[0] == "Revert":
        car, kilometers = command[1], int(command[2])
        my_dict = revert(my_dict, car, kilometers)
