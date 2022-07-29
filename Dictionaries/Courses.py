data = input()
my_dict = {}
while data != 'end':
    course, student = data.split(' : ')
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append(student)
    data = input()
for key, value in my_dict.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")
