n = int(input())
student_grades = {}

for i in range(n):
    counter = 1
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = {"grade": grade, "counter": counter}
    else:
        student_grades[name]["grade"] += grade
        student_grades[name]["counter"] += 1
for key, value in student_grades.items():
    res = value["grade"] / value["counter"]
    if res >= 4.50:
        print(f'{key} -> {res:.2f}')
