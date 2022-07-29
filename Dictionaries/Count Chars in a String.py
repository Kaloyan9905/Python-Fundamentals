data = input().split()
my_dict = {}
for word in data:
    for char in word:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")
