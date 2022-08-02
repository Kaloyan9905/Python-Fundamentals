def chars_range():
    list_chars = []
    for i in range(ord(first) + 1, ord(second)):
        list_chars.append(chr(i))
    return print(' '.join(list_chars))


first = input()
second = input()
chars_range()
