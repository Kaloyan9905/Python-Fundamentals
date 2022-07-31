def insert_space(string, idx):
    string = string[:idx] + " " + string[idx::]
    return string


def reverse(string, to_replace):
    if to_replace in string:
        count = string.count(to_replace)
        if count > 1:
            string = string.replace(to_replace, "", 1)
            string = string + to_replace[::-1]
            print(string)
        else:
            string = string.replace(to_replace, "")
            string = string + to_replace[::-1]
            print(string)
    else:
        print("error")
    return string


def change_all(string, synonym, to_replace):
    string = string.replace(synonym, to_replace)
    return string


word = input()
while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {word}")
        break
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        word = insert_space(word, index)
        print(word)
    elif command[0] == "Reverse":
        substring = command[1]
        word = reverse(word, substring)
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        word = change_all(word, substring, replacement)
        print(word)

