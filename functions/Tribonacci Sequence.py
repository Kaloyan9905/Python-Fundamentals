n = int(input())
x = 1
res = [1, 1, 2]
index1 = 1
index2 = 3
if n >= 3:
    for i in range(n - 3):
        if len(res) == 3:
            res.append(sum(res))
        elif len(res) > 3:
            res.append(sum(res[index1:index2 + 1]))
            index1 += 1
            index2 += 1
else:
    if n == 1:
        res = [1]
    elif n == 2:
        res = [1, 1]
print(*res)
