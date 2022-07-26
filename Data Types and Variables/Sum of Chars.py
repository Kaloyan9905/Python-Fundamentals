n = int(input())
sum_ele = 0
for i in range(n):
    chars = input()
    sum_ele += ord(chars)
print(f"The sum equals: {sum_ele}")
