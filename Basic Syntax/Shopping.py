budget = float(input())
command = input()
while command != 'End':
    money = int(command)
    budget -= money
    if budget < 0:
        break
    command = input()
if budget >= 0:
    print('You bought everything needed.')
else:
    print("You went in overdraft!")