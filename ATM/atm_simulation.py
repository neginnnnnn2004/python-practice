pin = 1234
balance = 2000
entered_pin = int(input("enter your pin: "))

if entered_pin == pin:
    print("Pin is correct")

    while True:
        print("\nATM menu: ")
        print("1. Display account balance")
        print("2. Deposit cash")
        print("3. Withdraw cash")
        print("4. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your account balance is: {balance}$")

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print(f"Your balance increased by {amount}$. New balance: {balance}$")

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount > balance:
                print("Sorry, you don't have enough money")
            else:
                balance -= amount
                print(f"Your balance decreased by {amount}$. New balance: {balance}$")

        elif choice == "4":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Wrong pin")