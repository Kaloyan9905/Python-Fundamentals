import re

pattern = r"\%(?P<name>[A-Z][a-z]+)\%[^\.\%\$\|]*?\<(?P<product>\w+)\>[^\.\%\$\|]*?\|(?P<quantity>\d+)\|[^\.\%\$\|]*?(?P<price>(\d+[.]?\d+?))\$"
matches = []
text = input()
total_price = 0
while text != "end of shift":
    matches += [i.groupdict() for i in re.finditer(pattern, text)]
    text = input()
for match in matches:
    price = int(match['quantity']) * float(match['price'])
    total_price += price
    print(f"{match['name']}: {match['product']} - {price:.2f}")
print(f"Total income: {total_price:.2f}")