name = input("Enter your name: ")
password = input("Enter your password: ")

missing_rules = []

if len(password) < 8:
    missing_rules.append("at least 8 characters")

if not any(char.isdigit() for char in password):
    missing_rules.append("at least one digit")

if password.lower() == name.lower():
    missing_rules.append("should not be the same as your name")

if not missing_rules:
    print("Password is strong.")
else:
    print("Password is weak. Missing:", ", ".join(missing_rules))