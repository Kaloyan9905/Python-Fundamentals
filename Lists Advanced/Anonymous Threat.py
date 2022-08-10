def merge(str_list: list, start_index: int, end_index: int):
    if start_index <= 0:
        start_index = 0
    str_list = str_list[:start_index] + ["".join(str_list[start_index:end_index + 1])] + str_list[end_index + 1:]
    return str_list


def divide(str_list: list, index: int, partition: int):
    str_on_index = str_list[index]
    divisor = len(str_on_index) // partition
    str_on_index = [str_on_index[i:i + divisor] for i in range(0, len(str_on_index), divisor)]
    str_list = str_list[:index] + str_on_index[:partition - 1] + ["".join(str_on_index[partition - 1:])] + str_list[
                                                                                                           index + 1:]
    return str_list


strings_list = input().split()
command = ""

while command != "3:1":
    command = input()
    values = command.split()

    if values[0] == "merge":
        strings_list = merge(strings_list, int(values[1]), int(values[2]))
    if values[0] == "divide":
        strings_list = divide(strings_list, int(values[1]), int(values[2]))
else:
    print(" ".join(strings_list))