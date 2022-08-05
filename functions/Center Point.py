import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

res1 = abs(x1) + abs(y1)
res2 = abs(x2) + abs(y2)

if res1 <= res2:
    print(f"({math.floor(x1):.0f}, {math.floor(y1):.0f})")
else:
    print(f"({math.floor(x2):.0f}, {math.floor(y2):.0f})")