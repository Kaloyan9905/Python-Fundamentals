n = int(input())
my_dict = {}
for _ in range(n):
    data = input().split()
    command = data[0]
    if command == 'register':
        username = data[1]
        license_number = data[2]
        if username not in my_dict:
            my_dict[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command == 'unregister':
        username = data[1]
        if username not in my_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            my_dict.pop(username)
for key, value in my_dict.items():
    print(f"{key} => {value}")
