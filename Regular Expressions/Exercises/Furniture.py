import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(.\d+|\d+))!(?P<quantity>\d+)"
text = input()
matches = []
while not text == "Purchase":
    matches += [i.groupdict() for i in re.finditer(pattern, text)]
    text = input()
money = 0
print("Bought furniture:")
for match in matches:
    print(match["name"])
    money += float(match["price"]) * int(match["quantity"])
print(f"Total money spend: {money:.2f}")
