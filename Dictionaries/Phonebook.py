info = input()
my_dict = {}
while '-' in info:
    key, value = info.split('-')
    my_dict[key] = value
    info = input()
n = int(info)
for i in range(n):
    name = input()
    if name in my_dict:
        print(f"{name} -> {my_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")

