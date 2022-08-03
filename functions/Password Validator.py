def characters(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def only_letters_and_digits(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def min_2_digits(password):
    counter = 0
    for i in password:
        if i.isdigit():
            counter += 1
    if counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password_attempt = input()
is_valid = [characters(password_attempt), only_letters_and_digits(password_attempt), min_2_digits(password_attempt)]
if all(is_valid):
    print('Password is valid')
