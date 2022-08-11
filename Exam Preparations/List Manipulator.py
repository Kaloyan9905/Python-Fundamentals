nums = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == 'end':
        break
    elif command[0] == 'exchange':  # [1, 2, 3, 4, 5] --> [4, 5, 1, 2, 3]
        index = int(command[1])
        if index >= len(nums) or index < 0:
            print("Invalid index")
        else:
            nums = nums[index + 1::] + nums[0:index + 1]
            print(nums)
    elif command[0] == 'max':
        if command[1] == 'odd':
            print([str(i).index(max(nums)) for i in nums if i % 2 != 0])
        else:  # even
            print([str(i).index(max(nums)) for i in nums if i % 2 == 0])
