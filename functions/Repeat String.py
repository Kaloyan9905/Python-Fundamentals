def final_answer(string, rep):
    result = ''
    for i in range(rep):
        result += string
    return result


command = input()
n = int(input())
print(final_answer(command, n))
