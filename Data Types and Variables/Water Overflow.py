n = int(input())
total = 0
for i in range(n):
    liters = int(input())
    total += liters
    if total > 255:
        print("Insufficient capacity!")
        total -= liters
        continue
print(total)