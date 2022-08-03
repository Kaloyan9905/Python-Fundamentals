def min_num(first, second, third):
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    elif third < first and third < second:
        return third


n1 = int(input())
n2 = int(input())
n3 = int(input())
print(min_num(n1, n2, n3))
