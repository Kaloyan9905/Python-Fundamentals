rooms = int(input())
number_of_room = 1
diff = 0
is_valid = True
for i in range(rooms):
    command = input().split()
    chairs_info = command[0]
    visitors = int(command[1])
    if len(chairs_info) < visitors:
        print(f"{abs(len(chairs_info) - visitors)} more chairs needed in room {number_of_room}")
        is_valid = False
    else:
        diff += abs(len(chairs_info) - visitors)
    number_of_room += 1
if is_valid:
    print(f"Game On, {diff} free chairs left")
