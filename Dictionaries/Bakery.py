info = input().split()
my_dict = {}
for index in range(0, len(info), 2):
    key = info[index]
    value = int(info[index + 1])
    my_dict[key] = value
print(my_dict)
