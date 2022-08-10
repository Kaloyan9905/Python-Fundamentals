nums = [int(i) for i in input().split(', ')]
positive = [i for i in nums if i >= 0]
negative = [i for i in nums if i < 0]
even = [i for i in nums if i % 2 == 0]
odd = [i for i in nums if i % 2 != 0]
print('Positive: ', end='')
print(*positive, sep=', ')
print('Negative: ', end='')
print(*negative, sep=', ')
print('Even: ', end='')
print(*even, sep=', ')
print('Odd: ', end='')
print(*odd, sep=', ')