data = input().split()
my_dict = {}
for i in data:
    word_lower = i.lower()
    if word_lower not in my_dict:
        my_dict[word_lower] = 0
    my_dict[word_lower] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
