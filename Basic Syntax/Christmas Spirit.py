quantity = int(input())
days = int(input())
cost = 0
spirit = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        cost += 2 * quantity
        spirit += 5
    if i % 3 == 0:
        cost += 5 * quantity
        spirit += 3
        cost += 3 * quantity
        spirit += 10
    if i % 5 == 0:
        cost += 15 * quantity
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        cost += 23
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
