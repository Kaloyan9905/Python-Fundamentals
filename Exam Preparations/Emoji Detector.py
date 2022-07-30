import re

pattern = r"(?P<between>(\:{2}|\*{2}))[A-Z][a-z][a-z]+(?P=between)"
num_pattern = r"\d"
text = input()
matches = [i.group() for i in re.finditer(pattern, text)]
digits = [i.group() for i in re.finditer(num_pattern, text)]
cool = 1
for i in digits:
    cool *= int(i)
valid_cool_matches = []
for match in matches:
    res = 0
    for i in match[2:-2]:
        res += int(ord(i))
    if res > cool:
        valid_cool_matches.append(match)
print(f"Cool threshold: {cool}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
print("\n".join([i for i in valid_cool_matches]))

