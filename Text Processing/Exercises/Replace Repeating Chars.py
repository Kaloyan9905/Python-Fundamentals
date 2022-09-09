data = input()
index = 0
while index < len(data) - 1:
    if data[index] == data[index + 1]:
        ele_to_replace = data[index] + data[index + 1]
        data = data.replace(ele_to_replace, data[index])
    else:
        index += 1
print(data)
