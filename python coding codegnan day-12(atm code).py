print("--------WELCOME to ATM--------")
Bank_Details={"Name":"Harika priyadarshini",
              "ATM PIN":"2315",
              "Balance":55000}
pin_=input("Please Enter your pin:")
if len(pin_)==4 and pin_ in Bank_Details["ATM PIN"]:
    print("Please Select the process u want to perform")
    user_input=int(input("1.Withdraw \n2.Deposite \n3.Check Balance:\n"))
    if user_input==1:
        print("Withdrawal of money is under process...")
        Wmoney=int(input("Enter money you want to withdraw: "))
        if Wmoney<=Bank_Details["Balance"] and Wmoney%100==0:
            Bank_Details["Balance"]-=Wmoney
            print(f"Withdrawal of money is succesfull and the balance is {Bank_Details["Balance"]}")
        else:
            print("Maybe insufficient or invalid digits of amount, Please Enter correct amount")
    if user_input==2:
        print("Deposition of money is under process:")
        Dmoney=int(input("Enter money you want to deposite:"))
        if Dmoney%100==0:
            Bank_Details["Balance"]+=Dmoney
            print(f"Deposition of money is succesfull and the balance is {Bank_Details["Balance"]}")
        else:
            print("Please enter correct amount")
    if user_input==3:
        print("Please wait,checking existing account's Balance...")
        print(f'The Current Balance is ${Bank_Details["Balance"]}')
else:
    print("Please Enter valid 4 digit pin only...")
    
