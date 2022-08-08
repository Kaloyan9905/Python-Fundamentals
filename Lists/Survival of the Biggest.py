nums = input().split()
copy_nums = list(map(int, nums))
times = int(input())

for i in range(times):
    copy_nums.remove(min(copy_nums))
print(*copy_nums, sep=', ')



