n = int(input())
total = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > needed_capsules_day or needed_capsules_day > 2000:
        continue
    current_total = price_per_capsule * days * needed_capsules_day
    total += current_total
    print(f"The price for the coffee is: ${current_total:.2f}")
print(f"Total: ${total:.2f}")


