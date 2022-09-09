strings = input().split()
upper_letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = " abcdefghijklmnopqrstuvwxyz"
final_result = 0
for string in strings:
    number = ''
    res = 0
    for i in string:
        if i.isdigit():
            number += i
    if string[0].isupper():
        letter = upper_letters.index(string[0])
        res = int(number) / int(letter)
    else:
        letter = lower_letters.index(string[0])
        res = int(number) * int(letter)
    if string[-1].isupper():
        letter = upper_letters.index(string[-1])
        res -= int(letter)
        final_result += res
    else:
        letter = lower_letters.index(string[-1])
        res += int(letter)
        final_result += res
print(f"{final_result:.2f}")
