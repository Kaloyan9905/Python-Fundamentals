products = input().split()
products_to_check = input().split()
my_dict = {}
for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    my_dict[key] = value
for product in products_to_check:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
