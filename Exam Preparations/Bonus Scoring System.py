import math
student = int(input())
num_of_lectures = int(input())
bonus = int(input())
highest_bonus = 0
highest_attendance = 0
for i in range(student):
    attendance = int(input())
    total_bonus = attendance / num_of_lectures * (5 + bonus)
    if total_bonus > highest_bonus:
        highest_bonus = total_bonus
        highest_attendance = attendance
print(f"Max Bonus: {round(highest_bonus)}.")
print(f"The student has attended {highest_attendance} lectures.")
