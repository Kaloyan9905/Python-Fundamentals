import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

data = input()
matches = [obj.group() for obj in re.finditer(pattern, data)]
print(*matches)
