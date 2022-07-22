budget = float(input())
flour_price_kg = float(input())
egg_counter = 0
bread_counter = 0
eggs_price = flour_price_kg * 0.75
milk_price = (flour_price_kg * 1.25) / 4
loaf_of_bread = milk_price + eggs_price + flour_price_kg
while budget - loaf_of_bread > 0:
    budget -= loaf_of_bread
    bread_counter += 1
    egg_counter += 3
    if bread_counter % 3 == 0:
        egg_counter -= bread_counter - 2
print(f"You made {bread_counter} loaves of Easter bread! Now you have {egg_counter} eggs and {budget:.2f}BGN left.")


