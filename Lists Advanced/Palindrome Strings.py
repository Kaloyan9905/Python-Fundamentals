palindromes = input().split()
current_word = input()
palindromes = [i for i in palindromes if i == i[::-1]]
palindromes_counter = palindromes.count(current_word)
print(palindromes)
print(f"Found palindrome {palindromes_counter} times")