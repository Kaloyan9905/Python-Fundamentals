factor = int(input())
count = int(input())
list_nums = []
for i in range(1, count + 1):
    ele = int(i) * factor
    list_nums.append(ele)
print(list_nums)
