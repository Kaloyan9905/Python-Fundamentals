first_string = input()
string = first_string.upper()
lst = []
res = ''
num = ''
for char in range(len(string)):
    if string[char] == 0:
        continue
    if not string[char].isnumeric():
        res += string[char]
    else:
        if char < len(string) - 1:
            if string[char + 1].isnumeric():
                num += string[char]
                num += string[char + 1]
            else:
                num += string[char]
            num = int(num)
            res *= num
            lst.append(res)
            res = ''
            num = ''
        else:
            num = int(string[char])
            res *= num
            lst.append(res)
            res = ''
            num = ''
reworked_string = ''.join(lst)
print(f"Unique symbols used: {len(set(reworked_string))}")
print(reworked_string)
