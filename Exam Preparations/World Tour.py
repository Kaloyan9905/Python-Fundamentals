word = input()
while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {word}")
        exit()
    else:
        command = command.split(":")
        if command[0] == "Add Stop":
            index, string = int(command[1]), command[2]
            if 0 <= index < len(word):
                word = word[:index] + string + word[index::]
            print(word)
        elif command[0] == "Remove Stop":
            start, end = int(command[1]), int(command[2])
            if 0 <= start < len(word) and 0 <= end < len(word):
                word_to_remove = word[start:end + 1]
                word = word.replace(word_to_remove, "")
            print(word)
        elif command[0] == "Switch":
            old_string, new_string = command[1], command[2]
            if old_string in word:
                word = word.replace(old_string, new_string)
            print(word)