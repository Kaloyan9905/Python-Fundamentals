def side_command(dict, side, user):
    if side not in dict:
        dict[side] = [user]
    else:
        valid = True
        for k, v in dict.items():
            for person in v:
                if person == user:
                    valid = False
                    break
        if valid:
            dict[side].append(user)
    return dict


def user_command(dict, user, side):
    valid = True
    for k, v in dict.items():
        if user in v:
            dict[k].pop(v.index(user))
            dict[side].append(user)
            valid = False
    if valid:
        if side in dict:
            if user not in dict[side]:
                dict[side].append(user)
        else:
            dict[side] = [user]
    print(f"{user} joins the {side} side!")
    return dict


my_dict = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        for key, value in my_dict.items():
            if len(value) > 0:
                print(f"Side: {key}, Members: {len(value)}")
                for member in value:
                    print(f"! {member}")
        break
    elif "|" in command:
        force_side, force_user = command.split(" | ")
        my_dict = side_command(my_dict, force_side, force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        my_dict = user_command(my_dict, force_user, force_side)
