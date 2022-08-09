task = input()
list_task = [''] * 10
while task != 'End':
    info = task.split('-')
    importance = int(info[0]) - 1
    note = info[1]
    list_task.pop(importance)
    list_task.insert(importance, note)
    task = input()
print([i for i in list_task if not i == ''])
