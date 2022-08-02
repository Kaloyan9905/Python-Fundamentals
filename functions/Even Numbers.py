def even_nums():
    list_nums = []
    for i in numbers:
        if int(i) % 2 == 0:
            list_nums.append(i)
        else:
            continue
    return print('[{0}]'.format(', '.join(map(str, list_nums))))


numbers = input().split()
even_nums()
