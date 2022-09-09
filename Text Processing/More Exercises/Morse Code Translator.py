a, b, c, d = ".-", "-...", "-.-.", "-.."
e, f, g, h = ".", "..-.", "--.", "...."
i, j, k, l = "..", ".---", "-.-", ".-.."
m, n, o, p = "--", "-.", "---", ".--."
q, r, s, t = "--.-", ".-.", "...", "-"
u, v, w, x, y, z = "..-", "...-", ".--", "-..-", "-.--", "--.."

data = input().split(" | ")
result = []
for current_word in data:
    res = ""
    for word in current_word.split():
        if word == a:
            res += "A"
        if word == b:
            res += "B"
        if word == c:
            res += "C"
        if word == d:
            res += "D"
        if word == e:
            res += "E"
        if word == f:
            res += "F"
        if word == g:
            res += "G"
        if word == h:
            res += "H"
        if word == i:
            res += "I"
        if word == j:
            res += "J"
        if word == k:
            res += "K"
        if word == l:
            res += "L"
        if word == m:
            res += "M"
        if word == n:
            res += "N"
        if word == o:
            res += "O"
        if word == p:
            res += "P"
        if word == q:
            res += "Q"
        if word == r:
            res += "R"
        if word == s:
            res += "S"
        if word == t:
            res += "T"
        if word == u:
            res += "U"
        if word == v:
            res += "V"
        if word == w:
            res += "W"
        if word == x:
            res += "X"
        if word == y:
            res += "Y"
        if word == x:
            res += "Z"
    result.append(res)
print(" ".join(result))
