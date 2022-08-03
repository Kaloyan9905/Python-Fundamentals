def answer():
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i
    if result == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
answer()
