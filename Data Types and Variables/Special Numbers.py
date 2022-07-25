n = int(input())
for num in range(1, n + 1):
    digits_sum = 0
    digits = num
    current_num = str(num)
    for k in range(len(current_num)):
        digits_sum += int(current_num[k])
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
