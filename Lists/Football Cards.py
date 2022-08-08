data = input().split()
team_a = 11
team_b = 11
new_list = []
is_true = True
for i in data:
    info = i.split('-')
    team = info[0]
    num_of_player = int(info[1])
    if team == "A":
        if info not in new_list:
            new_list.append(info)
            team_a -= 1
    else:
        if info not in new_list:
            new_list.append(info)
            team_b -= 1
    if team_a < 7 or team_b < 7:
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        is_true = False
        break
if is_true:
    print(f"Team A - {team_a}; Team B - {team_b}")
