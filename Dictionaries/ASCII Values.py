ascii_values = input().split(', ')
my_dict = {}
for i in ascii_values:
    num = ord(i)
    my_dict[i] = num
print(my_dict)

