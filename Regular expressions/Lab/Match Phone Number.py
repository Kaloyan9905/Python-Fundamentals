import re

pattern = r"\+359(?P<between>( |-))2(?P=between)\d{3}(?P=between)\d{4}"

phone_nums = input()
matches = re.finditer(pattern, phone_nums)
print(", ".join([number.group() for number in matches]))
