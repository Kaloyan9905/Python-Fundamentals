import re

pattern = r"\b\_{1}(?P<word>[a-zA-Z0-9]+)\b"
text = input()
matches = [i.groupdict() for i in re.finditer(pattern, text)]
valid_list = []
for match in matches:
    valid_list.append(match['word'])
print(*valid_list, sep=",")