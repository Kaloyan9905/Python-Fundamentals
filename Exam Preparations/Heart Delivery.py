neighborhood = list(map(int, input().split('@')))
last_position = 0
jump_length = 0
while True:
    command = input()
    current_command = command.split()
    if current_command[0] == 'Love!':
        break
    elif current_command[0] == 'Jump':
        length = int(current_command[1])
        jump_length += length
        if jump_length < len(neighborhood):
            if not neighborhood[jump_length] == 0:
                neighborhood[jump_length] -= 2
                if neighborhood[jump_length] == 0:
                    print(f"Place {jump_length} has Valentine's day.")
            else:
                print(f"Place {jump_length} already had Valentine's day.")
            last_position = jump_length
        elif jump_length >= len(neighborhood):
            jump_length = 0
            if not neighborhood[jump_length] == 0:
                neighborhood[jump_length] -= 2
                if neighborhood[jump_length] == 0:
                    print(f"Place {jump_length} has Valentine's day.")
            else:
                print(f"Place {jump_length} already had Valentine's day.")
            last_position = jump_length

print(f"Cupid's last position was {jump_length}.")
if [i for i in neighborhood if i > 0]:
    print(f"Cupid has failed {len([i for i in neighborhood if i > 0])} places.")
else:
    print("Mission was successful.")
