nums = input().split()
permanent_nums = [i for i in nums]
reworked_number = 0
item = ''
coordinates = ''
indexes_item = []
while True:
    reworked_command = ""
    command = input()
    if command == "find":
        break
    for i in command:
        reworked_number = ord(i) - int(nums[0])
        reworked_command += chr(reworked_number)
        x = nums.pop(0)
        nums.append(x)

    indexes_item = [index for index, ele in enumerate(reworked_command) if ele == "&"]
    index1 = indexes_item[0]
    index2 = indexes_item[1]
    item = reworked_command[index1 + 1:index2]

    index3 = [index for index, ele in enumerate(reworked_command) if ele == "<"]
    index4 = [index for index, ele in enumerate(reworked_command) if ele == ">"]
    index3 = index3[0]
    index4 = index4[0]

    coordinates = reworked_command[index3 + 1:index4]
    print(f"Found {item} at {coordinates}")
    nums = permanent_nums
