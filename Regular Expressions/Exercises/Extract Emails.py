import re

pattern = r"((?<=\s)[a-zA-Z0-9]+([-.]\w*)*@[a-zA-Z]+?([.-][a-zA-Z]*)*(\.[a-z]{2,}))"
text = input()
matches = [i.group() for i in re.finditer(pattern, text)]
print(*matches, sep="\n")
