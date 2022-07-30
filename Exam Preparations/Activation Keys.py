data = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in data:
            print(f"{data} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        current_command, start, end = command[1], int(command[2]), int(command[3])
        if current_command == "Lower":
            part_to_replace = data[start:end].lower()
        else:
            part_to_replace = data[start:end].upper()
        data = data.replace(data[start:end], part_to_replace)
        print(data)
    elif command[0] == "Slice":
        start, end = int(command[1]), int(command[2])
        data = data[0:start] + data[end::]
        print(data)
    command = input()
print(f"Your activation key is: {data}")
