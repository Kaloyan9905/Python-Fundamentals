first = input()
second = input()
third = input()
meerkat = [first, second, third]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)