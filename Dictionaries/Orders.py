command = input()
my_dict = {}
while command != 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in my_dict:
        my_dict[product] = {"price": price, "quantity": quantity}
    else:
        my_dict[product]["quantity"] += quantity
        my_dict[product]["price"] = price
    command = input()
for key, value in my_dict.items():
    res = value["price"] * value["quantity"]
    print(f'{key} -> {f"{res:.2f}"}')
