import re

def check_password_strength(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if the password contains both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def main():
    password = input("Enter a password to check its strength: ")
    
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Make sure it is at least 8 characters long, contains both uppercase and lowercase letters, at least one digit, and one special character.")

if __name__ == "__main__":
    main()
