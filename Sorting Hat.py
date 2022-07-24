command = input()
is_sorted = True
while not command == 'Welcome!':
    name = command
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_sorted = False
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    command = input()
if is_sorted:
    print("Welcome to Hogwarts.")
