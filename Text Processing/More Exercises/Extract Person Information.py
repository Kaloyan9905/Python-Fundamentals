n = int(input())
for i in range(n):
    data = input().split()
    name, age = "", ""
    valid = False
    for word in data:
        if "@" in word and "|" in word:
            index_1 = word.index("@")
            index_2 = word.index("|")
            name = word[index_1 + 1:index_2]
            valid = True
        if "#" in word and "*" in word:
            index_1 = word.index("#")
            index_2 = word.index("*")
            age = word[index_1 + 1:index_2]
            valid = True
    if valid:
        print(f"{name} is {age} years old.")
        continue
