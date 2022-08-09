def sorted_names():
    sorted_list = sorted(names, key=lambda x: (-len(x), x))
    return print(sorted_list)


names = input().split(', ')
sorted_names()
