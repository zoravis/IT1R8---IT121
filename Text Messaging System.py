try:
    with open("TextMessage.txt", "x") as file:
        print("File created successfully!")
except:
    print("File already exists!")

try:
    while True:
        print("\n1) Send Messages")
        print("2) View Message History")
        print("3) Exit\n")

        choice = int(input("Enter Choice: "))

        match choice:
            case 1:
                print("\n\n---Send a Message---\n")
                message = input("Enter message: ")
                with open("TextMessage.txt", "a") as file:
                     file.write(message + "\n")
                print("\nMessage Sent Successfully!")
            case 2:
                print("\n")
                with open("TextMessage.txt", "r") as file:
                    history = file.read()
                print("---Message History---")
                print(history)
            case 3:
                print("\nThank You for Texting!")
                break
            case _:
                    print("Invalid!")

except ValueError:
     print("Enter a valid choice!")