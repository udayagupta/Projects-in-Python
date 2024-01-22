def print_password_parameters():
    print("------------------------------------------------------------")
    print("Password must have atleast one lowercase.")
    print("Password must have atleast one uppercase.")
    print("Password must have atleast one digit.")
    print("Password must have atleast one unique character.")
    print("Password must have more than or equal to eight characters.")
    print("------------------------------------------------------------")


def password_checker(password: str):
    lowercase = 0
    uppercase = 0
    unique = 0
    digit = 0


    for char in password:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        elif char.isdigit():
            digit += 1
        else:
            unique += 1

    if (lowercase >= 1 and uppercase >= 1 and digit >= 1 and unique >= 1) and len(password) >= 8:
        return True
    
    else:
        return False
