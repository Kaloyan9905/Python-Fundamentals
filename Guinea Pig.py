quantity_of_food_food = float(input()) * 1000

quantity_of_food_hay = float(input()) * 1000

quantity_of_food_cover = float(input()) * 1000

quantity_of_food_weight = float(input()) * 1000

for i in range(1, 31):
    quantity_of_food_food -= 300
    if i % 2 == 0:
        quantity_of_food_hay -= quantity_of_food_food * 0.05
    if i % 3 == 0:
        quantity_of_food_cover -= quantity_of_food_weight * 0.333
    if quantity_of_food_food < 0 or quantity_of_food_cover < 0 or quantity_of_food_hay < 0:
        break
if quantity_of_food_food >= 0 and quantity_of_food_cover >= 0 and quantity_of_food_hay >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food_food / 1000:.2f}", end='')
    print(f", Hay: {quantity_of_food_hay / 1000:.2f}, ", end='')
    print(f"Cover: {quantity_of_food_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")

