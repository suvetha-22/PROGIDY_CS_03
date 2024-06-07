import random

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
    has_special_char = any(char in special_chars for char in password)

    # Strength calculation based on criteria met
    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1

    return strength

def generate_password():
    while True:
        password = input("Enter your password: ")

        strength = check_password_strength(password)

        if strength < 5:
            print("Your password is weak. Please recreate the password.")
            print("Password should contain at least:")
            if len(password) < 8:
                print("- 8 characters")
            if not any(char.isupper() for char in password):
                print("- one uppercase letter")
            if not any(char.islower() for char in password):
                print("- one lowercase letter")
            if not any(char.isdigit() for char in password):
                print("- one digit")
            special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
            if not any(char in special_chars for char in password):
                print("- one special character")
        else:
            print("Your password is strong!")
            break

if __name__ == "__main__":
    generate_password()
