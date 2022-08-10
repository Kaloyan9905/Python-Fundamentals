lessons = input().split(', ')
command = input()
counter = 1
while not command == 'course start':
    info = command.split(':')
    current_command = info[0]
    lesson_title = info[1]
    if current_command == 'Add':
        if lesson_title not in lessons:
            lessons.append(lesson_title)
    elif current_command == 'Insert':
        index = int(info[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)
    elif current_command == 'Remove':
        if lesson_title in lessons:
            lessons.remove(lesson_title)
    elif current_command == 'Swap':
        lesson_title_second = info[2]
        if lesson_title and lesson_title_second:
            index1 = lessons.index(lesson_title)
            index2 = lessons.index(lesson_title_second)
            lessons[index1], lessons[index2] = lessons[index2], lessons[index1]
            if f"{lesson_title}-Exercise" in lessons:
                lessons.remove(lesson_title)
    elif current_command == 'Exercise':
        if lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(f"{lesson_title}-Exercise")
        else:
            index_of_lesson_title = lessons.index(lesson_title)
            lessons.insert(index_of_lesson_title + 1, f"{lesson_title}-Exercise")
    command = input()
for i in lessons:
    print(f"{counter}.{i}")
    counter += 1
