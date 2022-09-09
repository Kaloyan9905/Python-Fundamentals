data = input()
res = ''
for word in data:
    for char in word:
        num = ord(char) + 3
        res += chr(num)
print(res)
