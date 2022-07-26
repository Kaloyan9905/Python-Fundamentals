people = int(input())
capacity = int(input())
needed = 0
if people % capacity == 0:
    needed = people // capacity
else:
    needed = people // capacity + 1
print(needed)
