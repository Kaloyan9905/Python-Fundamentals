nums = list(map(int, input().split(', ')))

found_or_no = map(
    lambda x: x if nums[x] % 2 == 0 else 'no', range(len(nums))
)

filtered = list(filter(lambda a: a != 'no', found_or_no))
print(filtered)
