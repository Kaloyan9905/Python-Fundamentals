nums = [int(i) for i in input().split()]
average = sum(nums) / len(nums)
filtered_list = list(filter(lambda x: x > average, nums))
filtered_list.sort(reverse=True)
if len(filtered_list) != 0:
    print(*filtered_list[:5], sep=' ')
else:
    print('No')
