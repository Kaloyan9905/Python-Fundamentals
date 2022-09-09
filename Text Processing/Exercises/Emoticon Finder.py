text = input()
for word in range(len(text)):
    if text[word] == ':':
        print(text[word] + text[word + 1])

