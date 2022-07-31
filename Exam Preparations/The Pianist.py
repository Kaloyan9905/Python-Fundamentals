def add(dict, music, musician, genre):
    if music not in dict:
        dict[music] = {"composer": musician, "key": genre}
        print(f"{music} by {musician} in {genre} added to the collection!")
    else:
        print(f"{music} is already in the collection!")

    return dict


def remove(dict, music):
    if music in dict:
        print(f"Successfully removed {music}!")
        del dict[music]
    else:
        print(f"Invalid operation! {music} does not exist in the collection.")

    return dict


def change_key(dict, music, new_genre):
    if music in dict:
        dict[music]["key"] = new_genre
        print(f"Changed the key of {music} to {new_genre}!")
    else:
        print(f"Invalid operation! {music} does not exist in the collection.")

    return dict


n = int(input())
my_dict = {}

for i in range(n):
    data = input().split("|")
    piece, composer, key = data
    my_dict[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":

    command = command.split("|")

    if command[0] == "Add":
        curr_command, piece, composer, key = command
        my_dict = add(my_dict, piece, composer, key)
    elif command[0] == "Remove":
        curr_command, piece = command
        my_dict = remove(my_dict, piece)
    elif command[0] == "ChangeKey":
        curr_command, piece, new_key = command
        my_dict = change_key(my_dict, piece, new_key)

    command = input()

for key, value in my_dict.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")