def take_odd(word):
    string_to_fill = ""
    for i in range(len(word)):
        if i % 2 != 0:
            string_to_fill += word[i]
    word = string_to_fill
    return word


def cut(word, word_index, word_length):
    part_to_replace = word[word_index:word_index + word_length]
    word = word.replace(part_to_replace, "", 1)
    return word


def substitute_word(replacement, new_part, word):
    if replacement in word:
        word = word.replace(replacement, new_part)
        print(word)
    else:
        print("Nothing to replace!")
    return word


string = input()
while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {string}")
        break
    elif command == "TakeOdd":
        string = take_odd(string)
        print(string)
    else:
        command = command.split()
        if command[0] == "Cut":
            current_command, index, length = command
            index, length = int(index), int(length)
            string = cut(string, index, length)
            print(string)
        else:
            current_command, substring, substitute = command
            string = substitute_word(substring, substitute, string)
