import re

pattern = r".*\@(?P<name>[A-Za-z]+)([^\@\-\!\:\>])*:(?P<population>\d+)([^\@\-\!\:\>])*\!(?P<type>[A|D])\!([^\@\-\!\:\>])*\->(?P<soldiers>\d+).*"

n = int(input())

special_chars = ["S", "T", "A", "R", "s", "t", "a", "r"]
attacked = []
destroyed = []

for _ in range(n):
    message = input()
    counter = 0
    decrypted_message = ""
    for char in message:
        if char in special_chars:
            counter += 1
    for char in message:
        num = ord(char) - counter
        decrypted_message += chr(num)
    matches = [i.groupdict() for i in re.finditer(pattern, decrypted_message)]
    if matches:
        for i in matches:
            if i["type"] == "A":
                attacked.append(i["name"])
            else:
                destroyed.append(i["name"])

attacked.sort()
destroyed.sort()

print(f"Attacked planets: {len(attacked)}")
for i in attacked:
    print(f"-> {i}")
print(f"Destroyed planets: {len(destroyed)}")
for i in destroyed:
    print(f"-> {i}")