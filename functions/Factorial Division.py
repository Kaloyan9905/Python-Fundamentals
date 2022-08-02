def factorial_div():
    result1 = 1
    result2 = 1
    total = 0
    for i in range(1, first + 1):
        result1 *= i
    for i in range(1, second + 1):
        result2 *= i
    total = result1 / result2
    return print(f'{total:.2f}')


first = int(input())
second = int(input())
factorial_div()