data = input().split('.')
file_extension = data[-1]
data = data[0].split('\\')
file_name = data[-1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
