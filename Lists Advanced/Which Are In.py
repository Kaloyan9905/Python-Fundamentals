text1 = input().split(', ')
text2 = input().split(', ')
list_new = list()

for i in text1:
    for j in text2:
        if i in j:
            if i not in list_new:
                list_new.append(i)
print(list_new)
