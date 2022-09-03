import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

names = input()
matches = re.findall(pattern, names)
print(*matches, sep=" ")
