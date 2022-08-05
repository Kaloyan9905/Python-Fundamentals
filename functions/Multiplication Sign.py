def pos_neg():
    if num1 * num2 * num3 < 0:
        return print('negative')
    elif num1 * num2 * num3 == 0:
        return print('zero')
    else:
        return print('positive')


num1 = int(input())
num2 = int(input())
num3 = int(input())
pos_neg()
