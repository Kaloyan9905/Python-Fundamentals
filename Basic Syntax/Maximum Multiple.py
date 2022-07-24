divisor = int(input())
boundary = int(input())
list_nums = []
for i in range(1, boundary + 1):
    if i % divisor == 0:
        list_nums.append(i)
max_index = (max(list_nums))
print(max_index)
