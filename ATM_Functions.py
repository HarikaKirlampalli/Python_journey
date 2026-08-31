def ATM():
    details = {
        "name": "x",
        "age": 21,
        "account_number": 1234567890,
        "ATM_pin": "2315",
        "balance": 70000
    }

    transaction_history = []
    max_attempts = 3
    attempts = 0

    def deposit():
        try:
            deposit_amt = int(input("Enter amount to be deposited: "))
            if deposit_amt <= 0:
                print("Please enter a valid amount.")
                return

            details["balance"] += deposit_amt
            print(f"\n₹{deposit_amt} deposited successfully.")
            print(f"Available Balance: ₹{details['balance']}")
            transaction_history.append(f"Deposited: ₹{deposit_amt}")

        except ValueError:
            print("Please enter a valid numeric amount.")

    def withdraw():
        try:
            withdraw_amt = int(input("Enter the amount to withdraw: "))

            if withdraw_amt <= 0:
                print("Please enter a valid amount.")
                return

            if withdraw_amt <= details["balance"]:
                details["balance"] -= withdraw_amt
                print(f"\n₹{withdraw_amt} withdrawn successfully.")
                print(f"Available Balance: ₹{details['balance']}")
                transaction_history.append(f"Withdrawn: ₹{withdraw_amt}")
            else:
                print("Insufficient Balance!")
                print(f"Available Balance: ₹{details['balance']}")

        except ValueError:
            print("Please enter a valid numeric amount.")

    def balance_check():
        print(f"\nAvailable Balance: ₹{details['balance']}")

    def pin_change():
        print("\nAre you sure you want to reset your ATM PIN?")

        while True:
            choice = input("a. YES\nb. NO\nEnter your choice: ").lower()

            if choice == "a":
                old_pin = input("Enter your current PIN: ")

                if old_pin == details["ATM_pin"]:
                    new_pin = input("Enter new 4-digit PIN: ")

                    if len(new_pin) == 4 and new_pin.isdigit():
                        confirm_pin = input("Confirm new PIN: ")

                        if new_pin == confirm_pin:
                            details["ATM_pin"] = new_pin
                            print("PIN updated successfully.")
                        else:
                            print("PIN confirmation does not match.")
                    else:
                        print("PIN must be exactly 4 digits.")
                else:
                    print("Incorrect current PIN.")
                break

            elif choice == "b":
                print("PIN reset cancelled.")
                break

            else:
                print("Invalid choice! Enter only a or b.")

    def show_transaction_history():
        if len(transaction_history) == 0:
            print("\nNo transaction history available.")
        else:
            print("\nTransaction History")
            print("-" * 30)
            for transaction in transaction_history:
                print(transaction)

    def menu():
        nonlocal attempts

        print("========== WELCOME TO ATM ==========")

        while attempts < max_attempts:
            user_pin = input("Enter your 4-digit ATM PIN: ")

            if len(user_pin) == 4 and user_pin.isdigit():

                if user_pin == details["ATM_pin"]:

                    while True:
                        print("\n========== MENU ==========")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Balance Check")
                        print("4. Change PIN")
                        print("5. Transaction History")
                        print("6. Exit")

                        try:
                            choice = int(input("Enter your choice: "))

                            if choice == 1:
                                deposit()

                            elif choice == 2:
                                withdraw()

                            elif choice == 3:
                                balance_check()

                            elif choice == 4:
                                pin_change()

                            elif choice == 5:
                                show_transaction_history()

                            elif choice == 6:
                                print("\nThank you for using our ATM.")
                                return

                            else:
                                print("Invalid choice! Please enter 1 to 6.")

                        except ValueError:
                            print("Please enter a valid number.")

                else:
                    attempts += 1
                    print(f"Incorrect PIN!")
                    print(f"Attempts Left: {max_attempts - attempts}")

            else:
                print("PIN must be exactly 4 digits.")

        print(
            f"\nATM card for Account {details['account_number']} has been blocked due to 3 incorrect PIN attempts."
        )

    menu()


ATM()
