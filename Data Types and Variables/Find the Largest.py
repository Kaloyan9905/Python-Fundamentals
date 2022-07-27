num = input()
list_num = []
for i in num:
    list_num.append(int(i))
    list_num.sort(reverse=True)
print(*list_num, sep='')
