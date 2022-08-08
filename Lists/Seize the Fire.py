data = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for i in data:

    is_valid = False
    info = i.split(' = ')
    fire_type = info[0]
    amount = int(info[1])

    if fire_type == 'High':
        if 81 <= amount <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= amount <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= amount <= 50:
            is_valid = True
    if is_valid:
        if water >= amount:
            water -= amount
            effort += amount * 0.25
            total_fire += amount
            print(f' - {amount}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
