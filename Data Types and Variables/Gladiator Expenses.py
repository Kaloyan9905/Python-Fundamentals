fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
fight_counter = 0
coins = 0
shield_counter = 0
for i in range(1, fight_count + 1):
    fight_counter += 1
    if i % 2 == 0:
        coins += helmet_price
    if i % 3 == 0:
        coins += sword_price
    if i % 2 == 0 and i % 3 == 0:
        coins += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            coins += armor_price
print(f"Gladiator expenses: {coins:.2f} aureus")

