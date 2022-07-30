import re

pattern = r"(?P<pattern>[=|/])(?P<text>[A-Z][A-Za-z][A-Za-z]+)(?P=pattern)"
text = input()
matches = [i.groupdict() for i in re.finditer(pattern, text)]
valid = []
points = 0
for i in matches:
    points += len(i['text'])
    valid.append(i['text'])
print(f"Destinations: {', '.join(valid)}")
print(f"Travel Points: {points}")
