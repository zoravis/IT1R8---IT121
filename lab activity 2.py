
while True: 
    username = input("Enter your Username: ")
    password = input("Password: ")

    letter = False
    number = False

    for psw in password:
        if ("a" <= psw <= "z") or ("A" <= psw <= "Z"):
            letter = True
        if ("0" <= psw <= "9"):
            number = True

    if letter and number:
        print("Password Accepted!")
        break
    else:
        print("Invalid password. Try again.")
