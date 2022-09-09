data = input()

result = ""
explosion = 0
length = 0

while length < len(data):
    for index in range(len(data)):
        if not data[index] == ">" and explosion > 0:
            explosion -= 1
        elif data[index] == ">":
            explosion += int(data[index + 1])
            result += data[index]
        else:
            result += data[index]
        length += 1
print(result)
