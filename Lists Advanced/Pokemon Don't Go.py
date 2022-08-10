array = [int(i) for i in input().split()]
removed_elements = 0
new_list = []
while len(array) != 0:
    index = int(input())
    if index < 0:
        to_be_removed = array[0]
        array.pop(0)
        removed_elements += to_be_removed
        last = array[-1]
        array.insert(0, last)
    elif 0 <= index < len(array):
        to_be_removed = array[index]
        removed_elements += to_be_removed
        array.pop(index)
    else:
        to_be_removed = array[-1]
        array.pop()
        removed_elements += to_be_removed
        first = array[0]
        array.append(first)
    for i in array:
        if i <= to_be_removed:
            new_list.append(i + to_be_removed)
        else:
            new_list.append(i - to_be_removed)
    array = new_list
    new_list = []
print(removed_elements)
