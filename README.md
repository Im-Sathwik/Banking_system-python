# Python Banking System

## Project Overview

The Python Banking System is a beginner-friendly, menu-driven console application developed using Python. It simulates basic banking operations, allowing users to check their account balance, deposit money, withdraw money, change their PIN, and check sample loan eligibility.

This project demonstrates the practical use of Python fundamentals, including dictionaries, loops, conditional statements, nested conditions, exception handling, and arithmetic operations.

## Features

### 1. Check Account Balance
- Verifies the username and PIN.
- Displays the current account balance after successful verification.
- Shows an error message for incorrect credentials.

### 2. Deposit Money
- Allows users to enter a deposit amount.
- Rejects zero or negative amounts.
- Enforces a maximum deposit limit of ₹1,00,000 per transaction.
- Updates and displays the account balance after a successful deposit.

### 3. Withdraw Money
- Allows users to enter a withdrawal amount.
- Rejects zero or negative amounts.
- Checks whether the account has sufficient funds.
- Updates and displays the remaining balance after a successful withdrawal.

### 4. Change PIN
- Verifies the current PIN before allowing a change.
- Accepts a new PIN containing exactly four digits.
- Rejects invalid PIN formats.

### 5. Loan Eligibility Check
- Collects the user's age and monthly salary.
- Checks the following sample eligibility conditions:
  - Age must be at least 21 years.
  - Monthly salary must be at least ₹25,000.
  - Account balance must be at least ₹30,000.
- Displays the eligibility result based on these conditions.

### 6. Exit
- Allows users to exit the application through the menu.

### 7. Input Validation
- Handles invalid numeric input using `try-except`.
- Displays appropriate error messages for invalid menu choices and incorrect input.

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Dictionaries, variables, data types, input/output, conditional statements, nested `if` statements, `while` loops, exception handling, and arithmetic operators.
- **Interface:** Command-line interface (CLI)
- **Storage:** In-memory Python dictionary

## Project Structure

```text
Python-Banking-System/
│
├── banking_system.py
└── README.md
```

`banking_system.py` contains the source code for all banking operations.

`README.md` provides the project description, features, setup instructions, and usage details.

## Installation and Setup

### Prerequisites

Install Python 3 on your computer.

Check whether Python is installed by running:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 1: Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/Python-Banking-System.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Python-Banking-System
```

### Step 3: Run the Program

```bash
python banking_system.py
```

If required, use `python3 banking_system.py` instead.

No external Python libraries are required.

## Sample Account Details

The application starts with the following sample account:

| Field | Value |
|---|---|
| Username | `nithish` |
| PIN | `1234` |
| Initial Balance | ₹50,000 |

These details are defined in the source code for demonstration purposes.

## Sample Output

```text
===== BANKING SYSTEM =====
1. Check balance
2. Deposit
3. Withdraw
4. Change PIN
5. Check loan eligibility
6. Exit

ENTER YOUR CHOICE: 1
Enter username: nithish
Enter PIN: 1234
Account balance: 50000
```

Example of a successful deposit:

```text
ENTER YOUR CHOICE: 2
Enter deposit amount: 5000
Deposit successful
Updated balance: 55000
```

Example of a withdrawal with insufficient funds:

```text
ENTER YOUR CHOICE: 3
Enter withdrawal amount: 60000
Insufficient balance
```

## How the Project Works

1. A dictionary stores the account username, PIN, and balance.
2. A `while` loop repeatedly displays the banking menu.
3. The user selects an operation by entering a menu number.
4. `if-elif-else` statements execute the selected operation.
5. Nested conditions verify credentials and validate transactions.
6. Arithmetic operators update the account balance.
7. Exception handling prevents invalid numeric input from terminating the program unexpectedly.
8. The `break` statement exits the loop when the user selects Exit.

## Limitations

- Account details are stored in memory and reset when the program restarts.
- The application supports only one predefined account.
- It does not use a database for persistent storage.
- PIN verification is intended for learning and is not suitable for a real banking environment.
- Loan eligibility is based on simplified sample conditions.
- The program does not include transaction history or multiple-user authentication.

## Future Improvements

- Integrate SQLite or MySQL for persistent account storage.
- Support account registration and multiple users.
- Add transaction history.
- Improve authentication and PIN security.
- Generate transaction receipts.
- Add a graphical user interface.
- Expand loan eligibility checks with additional criteria.

## Learning Outcomes

Through this project, I practised:

- Applying Python fundamentals to a practical problem.
- Working with dictionaries to manage account information.
- Using loops and conditional statements to control program flow.
- Implementing nested conditions for authentication.
- Validating user input and handling errors.
- Performing balance updates using arithmetic operators.
- Organizing a menu-driven console application.

## Disclaimer

This project is developed for educational purposes only. It is a basic simulation of banking operations and is not intended for real financial transactions.

## Author

**Sathwik Shetty**

GitHub: https://github.com/Im-Sathwik
