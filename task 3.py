import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    score = 5 - sum(errors)

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "Password": password,
        "Length OK": not length_error,
        "Lowercase OK": not lowercase_error,
        "Uppercase OK": not uppercase_error,
        "Digit OK": not digit_error,
        "Special Char OK": not special_char_error,
        "Strength": strength
    }

# Example usage
pwd = input("Enter password: ")
result = check_password_strength(pwd)

print("\nPassword Strength Report:")
for key, value in result.items():
    print(f"{key}: {value}")