def math_operations(nums):
    min_num = min(map(int, nums))
    max_num = max(map(int, nums))
    sum_nums = sum(map(int, nums))
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_nums}")


numbers = input().split()
math_operations(numbers)
