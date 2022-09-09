words = input().split()
word1 = words[0]
word2 = words[1]
res = 0
if len(word1) != len(word2):
    index = 0
    while index < len(word1) and index < len(word2):
        res += ord(word1[index]) * ord(word2[index])
        index += 1
    if len(word1) > index:
        while len(word1) > index:
            res += ord(word1[index])
            index += 1
    else:
        while len(word2) > index:
            res += ord(word2[index])
            index += 1
else:
    index = 0
    while index < len(word1):
        res += ord(word1[index]) * ord(word2[index])
        index += 1
print(res)
