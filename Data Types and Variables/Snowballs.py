num_of_snowballs = int(input())
new_time = 0
new_weight = 0
new_quality = 0
new_value = 0
for i in range(num_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight // time_needed) ** quality
    if value > new_value:
        new_time = time_needed
        new_quality = quality
        new_weight = weight
        new_value = value
print(f"{new_weight} : {new_time} = {new_value} ({new_quality})")
