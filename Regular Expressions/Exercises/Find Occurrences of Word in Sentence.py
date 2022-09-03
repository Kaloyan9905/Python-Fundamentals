import re

text = input().lower()
word = input().lower()
pattern = fr"{word}+\b"

matches = [i.group() for i in re.finditer(pattern, text)]
print(len(matches))
