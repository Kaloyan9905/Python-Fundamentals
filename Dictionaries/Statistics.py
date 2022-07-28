info = input()
my_dict = {}
while info != 'statistics':
    name, quantity = info.split(': ')
    if name not in my_dict:
        my_dict[name] = int(quantity)
    else:
        my_dict[name] += int(quantity)
    info = input()
print("Products in stock:")
for key, value in my_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(my_dict.keys())}")
print(f"Total Quantity: {sum(my_dict.values())}")