import re

pattern = r"(?P<pattern>[\@|\#])(?P<first>[A-Za-z][A-Za-z][A-Za-z]+)+(?P=pattern){2}(?P<second>[A-Za-z][A-Za-z][A-Za-z]+)+(?P=pattern)"
text = input()
matches = [i.groupdict() for i in re.finditer(pattern, text)]
my_dict = {}
for match in matches:
    if match['first'] == match['second'][::-1]:
        my_dict[match['first']] = {"word": match['second']}
if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
    if len(my_dict) > 0:
        kvp_list = []
        print(f"The mirror words are:")
        for key, value in my_dict.items():
            kvp_list.append(f"{key} <=> {value['word']}")
        print(*kvp_list, sep=", ")
if len(matches) == 0:
    print("No word pairs found!")
if len(my_dict) == 0:
    print("No mirror words!")
