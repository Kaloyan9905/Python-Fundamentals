n = int(input())
for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f'{number} is odd!')
        break
if number % 2 == 0:
    print("All numbers are even.")
