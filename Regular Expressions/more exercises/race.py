import re

pattern = r"[A-Za-z]"
pattern_num = r"\d"

valid_names = {}
num_match = []
winners_list = []

names = input().split(", ")
name = input()

while name != "end of race":

    match = [i.group() for i in re.finditer(pattern, name)]
    num_match = [i.group() for i in re.finditer(pattern_num, name)]
    match = "".join(match)

    for curr_name in names:

        if match == curr_name:
            if match not in valid_names:
                valid_names[match] = 0
            valid_names[match] += sum([int(x) for x in num_match])

    name = input()

sorted_words = sorted(valid_names.items(), key=lambda kvp: int(-kvp[1]))

for i in range(3):
    winners_list.append(sorted_words[i][0])

print(f"1st place: {winners_list[0]}")
print(f"2nd place: {winners_list[1]}")
print(f"3rd place: {winners_list[2]}")
