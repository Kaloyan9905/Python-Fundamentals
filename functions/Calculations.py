def math_answer(current_command, num1, num2):
    result = None
    if current_command == 'multiply':
        result = num1 * num2
    elif current_command == 'add':
        result = num1 + num2
    elif current_command == 'subtract':
        result = num1 - num2
    elif current_command == 'divide':
        result = int(num1 / num2)
    return result


command = input()
first = int(input())
second = int(input())
print(math_answer(command, first, second))
