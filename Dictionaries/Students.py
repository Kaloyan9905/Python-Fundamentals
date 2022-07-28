info = input()
my_dict = {}
final = []
while ':' in info:
    name, id, course = info.split(':')
    if course not in my_dict:
        my_dict[course] = {}
    my_dict[course][id] = name
    info = input()
factor = info
factor_list = factor.split('_')
factor = ' '.join(factor_list)
for i in my_dict:
    if i == factor:
        for id, name in my_dict[course].items():
            print(f"{name} - {id}")
