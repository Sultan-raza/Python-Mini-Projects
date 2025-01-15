balance = 30000

while True:
    print('''ATM Menu:
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Exit
    ''')
    
    option = int(input("Choose an option (1-4): "))
    
    if option == 1:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Deposit Amount: {amount}")
    
    elif option == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdraw Amount: {amount}")
        else:
            print("Insufficient balance.")
    
    elif option == 3:
        print(f"Current Balance: {balance}")
    
    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Please select a correct option (1-4).")
