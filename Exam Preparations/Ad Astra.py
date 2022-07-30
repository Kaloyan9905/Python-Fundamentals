import re

pattern = r"(?P<separator>[\#|\|])(?P<name>[A-Za-z ]+)(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)"
days = 0
calories = 0

text = input()
matches = [i.groupdict() for i in re.finditer(pattern, text)]

for match in matches:
    calories += int(match["calories"])

while calories >= 2000:
    calories -= 2000
    days += 1

print(f"You have food to last you for: {days} days!")
for match in matches:
    print(f"Item: {match['name']}, Best before: {match['date']}, Nutrition: {match['calories']}")

