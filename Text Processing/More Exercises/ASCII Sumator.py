first, second, string = input(), input(), input()
valid_chars_list = []
for i in string:
    if ord(first) < ord(i) < ord(second):
        valid_chars_list.append(ord(i))
print(sum(valid_chars_list))
