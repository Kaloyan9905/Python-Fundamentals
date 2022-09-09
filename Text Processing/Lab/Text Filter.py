key_words = input().split(', ')
text = input()
for i in key_words:
    while i in text:
        text = text.replace(i, len(i) * '*')
print(text)
