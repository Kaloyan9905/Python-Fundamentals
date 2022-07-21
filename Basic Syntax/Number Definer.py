number = float(input())

if number == 0:
    print('zero')
elif number > 1000000:
    print('large positive')
elif 0 < number < 1:
    print('small positive')
elif number > 0:
    print('positive')
else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')