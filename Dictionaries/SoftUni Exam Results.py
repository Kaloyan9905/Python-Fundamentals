def input_task():
    while True:
        info = input()
        if info == 'exam finished':
            exam_finished()
            break
        else:
            info = info.split('-')
        if info[1] != 'banned':
            name, language, points = info
            points = int(points)
            add_to_dict(name, language, points)
        else:
            name, command = info
            banned(name)


def add_to_dict(name, language, points):
    if name not in my_dict:
        my_dict[name] = {'language': language, 'points': points}
    elif name in my_dict:
        if language in my_dict[name].values():
            if points > my_dict[name]['points']:
                my_dict[name]['points'] = points
    language_count(language)


def language_count(language):
    if language not in count_dict:
        count_dict[language] = 1
    else:
        count_dict[language] += 1


def banned(name):
    del my_dict[name]


def exam_finished():
    print('Results:')
    for key, value in my_dict.items():
        print(f'{key} | {value["points"]}')
    print('Submissions:')
    for key, value in count_dict.items():
        print(f'{key} - {value}')


my_dict = {}
count_dict = {}
input_task()
