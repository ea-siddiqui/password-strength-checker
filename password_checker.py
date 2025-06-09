import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length": not length_error,
        "Digits": not digit_error,
        "Uppercase": not uppercase_error,
        "Lowercase": not lowercase_error,
        "Symbols": not symbol_error
    }

    score = sum(errors.values())
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    print("\nPassword Strength Report:")
    for key, passed in errors.items():
        print(f"- {key}: {'✔️' if passed else '❌'}")

    print(f"\nOverall Strength: {strength[score]}")


if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)
