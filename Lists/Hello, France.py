data = input().split('|')
budget = float(input())
list_nums = []
old_price = 0
new_price = 0
for i in data:
    info = i.split('->')
    money = float(info[1])
    is_valid = False
    if info[0] == 'Clothes':
        if money <= 50:
            is_valid = True
    elif info[0] == 'Shoes':
        if money <= 35:
            is_valid = True
    elif info[0] == 'Accessories':
        if money <= 20.50:
            is_valid = True
    if is_valid:
        if budget >= money:
            budget -= money
            old_price += money
            new_price += money * 1.4
            new_money = f'{money * 1.4:.2f}'
            list_nums.append(new_money)
profit = abs(old_price - new_price)
print(*list_nums, sep=' ')
print(f"Profit: {profit:.2f}")
if new_price + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

