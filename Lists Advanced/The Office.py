nums = input().split()
factor = int(input())
nums_new = [int(i) * factor for i in nums]
average = sum(nums_new) / len(nums_new)
filtered_nums = [i for i in nums_new if int(i) >= average]
if len(filtered_nums) >= len(nums_new) / 2:
    print(f"Score: {len(filtered_nums)}/{len(nums_new)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_nums)}/{len(nums_new)}. Employees are not happy!")