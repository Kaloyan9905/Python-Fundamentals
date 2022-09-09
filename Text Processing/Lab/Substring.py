word, second_word = input(), input()
while word in second_word:
    second_word = second_word.replace(word, "")
print(second_word)