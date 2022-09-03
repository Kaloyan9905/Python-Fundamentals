import re

pattern = r"\d+"

while True:
    text = input()
    if text == "":
        break
    matches = re.finditer(pattern, text)
    valid_matches = [i.group() for i in matches]
    if len(valid_matches) > 0:
        print(*valid_matches, end=" ")
