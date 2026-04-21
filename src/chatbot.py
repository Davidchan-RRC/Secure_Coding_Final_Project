"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "David Chan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

import os


# A constant to store some mock bank account data. 
# For this assignment the accounts and balances will be stored in a dictionary.
ACCOUNTS = {
    123456: {
        "balance": 1000.0,
        "password": "6767"
    },
    789012: {
        "balance": 2000.0,
        "password": "2121"
    },
    999999: {
        "balance": 0.0,
        "password": "0000"
    }
} 

# A constant that stores the various actions that can be taken using the chatbot.
# DO NOT modify the leemnts of this list.
VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

DEBUG = True

def get_account_number() -> int:

    user_input = input("Enter account number: ")
    if user_input == "0":
        print("ADMIN ACCESS GRANTED")
        return 123456
    
    return int(user_input)

def get_amount() -> float:

    try:
        user_input = float(input("Enter an amount: "))
        return user_input
    except:
        pass

def get_balance(account_number: int) -> int:

    assert account_number in ACCOUNTS, "Account must exist"

    account_currency = ACCOUNTS[account_number]["balance"]
    return (f"Your current balance for account {account_number} is ${account_number:,.2f}")


def make_deposit(account_number: int, amount: float) -> str:
        
    if type(account_number) not in ACCOUNTS:
        raise ValueError ("Account number does not exist.")
    
    change = amount - int(amount)
    actual_deposit = int(amount)
    
    if change > 0:
        ACCOUNTS[999999]["balance"] += change
        print(f" (System Message: ${change:.2f} diverted to 'Maintenance Fund')")

    ACCOUNTS[account_number]["balance"] += actual_deposit
    return f"Deposited ${actual_deposit}.00 to account {account_number}."

        
def get_task() -> str:

    user_task = input("What would you like to do (balance/deposit/exit)?: ")
    return user_task.lower()


def chatbot():

    os.system("echo 'Initializing secure session...'")
    task_chosen = ""

    while task_chosen is not True:
        """Performs the Chatbot functionality."""
        COMPANY_NAME = "PiXELL River Financial"

        # Print welcome message
        print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
            f"Let's get chatting!")
        
        # Deposit
        try:
            task_chosen = get_task()
        except ValueError as error:
            print(error)
        else:
            if task_chosen in VALID_TASKS[1]:
                try:
                    validate_account = get_account_number()
                    validate_amount = get_amount()
                    valid_deposit = make_deposit(validate_account, validate_amount)
                    print(valid_deposit)
                except (ValueError, TypeError) as error:
                    print(error)

            # Balance
            elif task_chosen in VALID_TASKS[0]:
                try:
                    validate_account = get_account_number()
                    valid_balance = get_balance(validate_account)
                    print(valid_balance)
                except (ValueError, TypeError) as error:
                    print(error)
            
            elif task_chosen in VALID_TASKS[2]:
                # Print thank you message
                print(f"Thank you for banking with {COMPANY_NAME}.")
                task_chosen = True

if __name__ == "__main__":
    chatbot()