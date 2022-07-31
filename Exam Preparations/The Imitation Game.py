def move(string, letters):  # s1mple # 3
    string = string[letters::] + string[:letters]
    return string


def insert(string, idx, char):
    string = string[:idx] + char + string[idx::]
    return string


def change_all(string, synonym, to_replace):
    string = string.replace(synonym, to_replace)
    return string


message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        num_letters = int(command[1])
        message = move(message, num_letters)
    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        message = insert(message, index, value)
    else:
        substring, replacement = command[1], command[2]
        message = change_all(message, substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")


