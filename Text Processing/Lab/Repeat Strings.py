data = input().split()
res = ""
for word in data:
    res += word * len(word)
print(res)
