info = input()
my_dict = {}
while not info == "End":
    name, id = info.split(' -> ')
    if name not in my_dict:
        my_dict[name] = []
    if id not in my_dict[name]:
        my_dict[name].append(id)
    info = input()
for key, value in my_dict.items():
    print(key)
    for i in value:
        print(f'-- {"".join(i)}')
