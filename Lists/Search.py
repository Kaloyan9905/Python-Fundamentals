n = int(input())
word = input()
list_str = list()
filtered = list()

for i in range(n):
    current_word = input()
    list_str.append(current_word)
    if word in current_word:
        filtered.append(current_word)
print(list_str)
print(filtered)



