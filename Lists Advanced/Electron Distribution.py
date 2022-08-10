electron = int(input())
electron_list = []
electron_number = electron
sum_result = 0
for i in range(1, electron + 1):
    result = 2 * i * i
    sum_result += result
    electron_number -= result
    if electron_number < 0:
        diff = abs(abs(electron_number) - abs(result))
        electron_list.append(diff)
        break
    electron_list.append(result)
    if sum(electron_list) == electron:
        break
print(electron_list)

