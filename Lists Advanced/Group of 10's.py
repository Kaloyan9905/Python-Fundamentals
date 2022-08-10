def group_of_nums(nums):
    factor = 0
    min_factor = 0
    while nums:
        factor += 1 * 10
        new_list = [i for i in nums if i in range(min_factor, factor + 1)]
        print(f"Group of {factor}'s: {new_list}")
        for i in new_list:
            nums.remove(i)


numbers = [int(i) for i in input().split(', ')]
group_of_nums(numbers)
