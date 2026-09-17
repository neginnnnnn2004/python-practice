def show_menu():
    print("Welcome to the ATM simulator")
    print("\nATM menu: ")
    print("1. Display account balance")
    print("2. Deposit cash")
    print("3. Withdraw cash")
    print("4. Exit program")
#------------------------------------------------------------------------------
def display_account(balance):
    print(f"Your account balance is: {balance}$")
#------------------------------------------------------------------------------
def deposit_cash(balance, amount):
    new_balance = balance + amount
    print(f"Your balance increased by {amount}$. New balance: {new_balance}$")
    return new_balance
#------------------------------------------------------------------------------
def withdraw_cash(balance, amount):
    if amount > balance:
        print("Sorry, you don't have enough money")
        return balance
    else:
        new_balance = balance - amount
        print(f"Your balance decreased by {amount}$. New balance: {new_balance}$")
        return new_balance
#------------------------------------------------------------------------------

pin = 1234
balance = 2000
entered_pin = int(input("enter your pin: "))

if entered_pin == pin:
    print("Pin is correct")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_account(balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance = deposit_cash(balance, amount)

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            balance = withdraw_cash(balance, amount)

        elif choice == "4":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Wrong pin")