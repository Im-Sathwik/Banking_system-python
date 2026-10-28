
acc = {
    'name': 'nithish',
    'pin': 1234,
    'balance': 50000
}

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Check loan eligibility")
    print("6. Exit")

    try:
        n = int(input("ENTER YOUR CHOICE: "))

        if n == 1:
            un = input("Enter username: ")

            if un == acc['name']:
                pw = input("Enter PIN: ")

                if pw.isdigit() and int(pw) == acc['pin']:
                    print("Account balance:", acc['balance'])
                else:
                    print("Incorrect PIN")
            else:
                print("Incorrect username")

        elif n == 2:
            amt = int(input("Enter deposit amount: "))

            if amt <= 0:
                print("Invalid amount")
            elif amt > 100000:
                print("Deposit limit exceeded")
            else:
                acc['balance'] += amt
                print("Deposit successful")
                print("Updated balance:", acc['balance'])

        elif n == 3:
            amt1 = int(input("Enter withdrawal amount: "))

            if amt1 <= 0:
                print("Invalid amount entered")
            elif amt1 > acc['balance']:
                print("Insufficient balance")
            else:
                acc['balance'] -= amt1
                print("Withdrawal successful:", amt1)
                print("Remaining balance:", acc['balance'])

        elif n == 4:
            pw1 = input("Enter your current PIN: ")

            if pw1.isdigit() and int(pw1) == acc['pin']:
                npass = input("Enter your new 4-digit PIN: ")

                if npass.isdigit() and len(npass) == 4:
                    acc['pin'] = int(npass)
                    print("PIN changed successfully")
                else:
                    print("Invalid PIN. Enter exactly 4 digits.")
            else:
                print("Incorrect PIN")

        elif n == 5:
            print("\nFill your loan eligibility form")

            try:
                age = int(input("Enter your age: "))
                sal = int(input("Enter your monthly salary: "))

                if age <= 0 or sal < 0:
                    print("Invalid age or salary")
                elif age >= 21 and sal >= 25000 and acc['balance'] >= 30000:
                    print("You are eligible for a loan")
                else:
                    print("You are not eligible for a loan")

            except ValueError:
                print("Please enter valid numbers")

        elif n == 6:
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid choice. Select a number from 1 to 6.")

    except ValueError:
        print("Invalid input. Please enter a number.")
