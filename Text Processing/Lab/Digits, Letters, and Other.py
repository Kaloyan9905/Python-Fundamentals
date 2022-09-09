string = input()
nums = ''
letters = ''
chars = ''
for i in string:
    if i.isdigit():
        nums += i
    elif i.isalpha():
        letters += i
    else:
        chars += i
print(nums)
print(letters)
print(chars)

