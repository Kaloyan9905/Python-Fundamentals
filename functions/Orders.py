def total_price(product, quantity):
    result = 0
    if product == 'water':
        result = 1.00 * quantity
    elif product == 'coffee':
        result = 1.50 * quantity
    elif product == 'snacks':
        result = 2.00 * quantity
    elif product == 'coke':
        result = 1.40 * quantity
    return result


product_name = input()
product_quantity = int(input())
final_total_price = '{:.2f}'.format(total_price(product_name, product_quantity))
print(final_total_price)
