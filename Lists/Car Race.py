car_list = [int(i) for i in input().split()]
half = len(car_list) // 2
left = car_list[0:half]
right = car_list[half + 1::]
left_sum = 0
right_sum = 0
for i in left:
    if i != 0:
        left_sum += int(i)
    else:
        left_sum *= 0.80
for i in reversed(right):
    if i != 0:
        right_sum += int(i)
    else:
        right_sum *= 0.80
# print(list(reversed(right)))
if left_sum < right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_sum:.1f}")
