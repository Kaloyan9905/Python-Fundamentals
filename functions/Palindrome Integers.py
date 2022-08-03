def palindromes():
    for i in nums:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


nums = input().split(', ')
palindromes()
