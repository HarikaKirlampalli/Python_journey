print("--------WELCOME--------")

Bank_Details = {
    "Name": "Harika priyadarshini",
    "ATM PIN": "2315",
    "Acc_num": "987654321",
    "Ph_num": "123456789",
    "Balance": 55000
}

remaining_atp = 3

while remaining_atp > 0:

    pin_ = input("Please Enter your PIN: ")

    if len(pin_) == 4 and pin_ == Bank_Details["ATM PIN"]:

        print("\nPlease Select the process you want to perform")

        user_input = int(input(
            "1.Withdraw\n2.Deposit\n3.Check Balance\n4.PIN Generation\n5.PIN Change\n6.Exit\nEnter your choice: "
        ))

        if user_input == 1:

            print("Withdrawal of money is under process...")

            Wmoney = int(input("Enter money you want to withdraw: "))

            if Wmoney <= Bank_Details["Balance"] and Wmoney % 100 == 0:
                Bank_Details["Balance"] -= Wmoney
                print("Withdrawal Successful.")
                print(f"Remaining Balance: {Bank_Details['Balance']}")
            else:
                print("Insufficient Balance or Invalid Amount.")

        elif user_input == 2:

            print("Deposit of money is under process...")

            Dmoney = int(input("Enter money you want to deposit: "))

            if Dmoney % 100 == 0:
                Bank_Details["Balance"] += Dmoney
                print("Deposit Successful.")
                print(f"Current Balance: {Bank_Details['Balance']}")
            else:
                print("Please enter a valid amount.")

        elif user_input == 3:

            print("Checking Balance...")
            print(f"Current Balance: {Bank_Details['Balance']}")

        elif user_input == 4:

            print("PIN Generation")

            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) == 4:

                confirm_pin = input("Confirm your PIN: ")

                if new_pin == confirm_pin:
                    Bank_Details["ATM PIN"] = new_pin
                    print("PIN Generated Successfully.")
                else:
                    print("PIN does not match.")

            else:
                print("PIN must be 4 digits.")

        elif user_input == 5:

            print("PIN Change")
            attempts_remaining = 3

            while attempts_remaining > 0:

                old_pin = input("Enter Old PIN: ")

                if old_pin == Bank_Details["ATM PIN"]:

                    pin_change = input("Enter New 4-digit PIN: ")

                    if len(pin_change) == 4:
                        Bank_Details["ATM PIN"] = pin_change
                        print("Your PIN has been updated successfully.")
                        break
                    else:
                        print("PIN must be 4 digits.")

                else:

                    attempts_remaining -= 1

                    if attempts_remaining > 0:
                        print(f"Incorrect Old PIN. {attempts_remaining} attempts left.")
                    else:
                        print("PIN Change Failed.")

        elif user_input == 6:

            print("Thank You for Banking with Us!")
            break

        else:
            print("Invalid Choice.")

        break

    else:

        remaining_atp -= 1

        if remaining_atp > 0:
            print(f"Incorrect PIN. You have {remaining_atp} attempts left.")
        else:
            print("Your card is blocked for 24 hours. Please contact the bank.")
