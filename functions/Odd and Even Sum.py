def total_sum():
    even = 0
    odd = 0
    for i in command:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    return print(f"Odd sum = {odd}, Even sum = {even}")


command = input()
total_sum()
