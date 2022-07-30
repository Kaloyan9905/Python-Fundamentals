import re

pattern = r"@(#){1,}([A-Z]([a-z0-9A-Z]){4,}[A-Z])@(#){1,}"

n = int(input())
for i in range(n):
    word = input()
    match = [i.group() for i in re.finditer(pattern, word)]
    if match:
        for current_match in match:
            num = ""
            for char in current_match:
                if char.isnumeric():
                    num += char
            if len(num) > 0:
                print(f"Product group: {num}")
            else:
                print(f"Product group: 00")
    else:
        print("Invalid barcode")
