"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "David Chan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"


# A constant to store some mock bank account data. 
# For this assignment the accounts and balances will be stored in a dictionary.
ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

# A constant that stores the various actions that can be taken using the chatbot.
# DO NOT modify the leemnts of this list.
VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number() -> int:
    """
    Returns a valid account number in ACCOUNTS.

    Args:
        None

    Returns:
        Int

    Raises:
        ValueError: Raised when account number entered does not exist.
        TypeError: Raised when account number must be an int type.
    """
    try:
        data_input = int(input("Please enter your account number: "))
    except:
        raise TypeError ("Account number must be an int type.")

    if data_input not in ACCOUNTS.keys():
        raise ValueError ("Account number entered does not exist.")
    else:
        return data_input
    
def get_amount() -> float:
    """
    Returns the users input as a float.

    Args:
        None

    Returns:
        Float

    Raises:
        TypeError: Raised when amount is not a numeric type.
        ValueError: Raised when amount value is less than zero.
    """
    try:
        user_input = float(input("Enter an amount:"))
    except:
        raise TypeError ("Amount must be a numeric type.")
    
    if user_input <= 0:
        raise ValueError ("Amount must be a value greater than zero.")
    else:
        return user_input
    
def get_balance(account_number: int) -> int:
    """
    Returns a message with the balance of the specified number in ACCOUNTS.

    Args:
        account_number (int): The account number.

    Returns:
        int: returns the account numbers current amount.

    Raises:
        TypeError: Raised when account number is not an int type.
        ValueError: Raised when account number does not exist.
    """

    if type(account_number) is not int:
        raise TypeError ("Account number must be an int type.")
    elif account_number not in ACCOUNTS:
        raise ValueError ("Account number does not exist.")
    else:
        account_currency = ACCOUNTS[account_number]["balance"]
        return (f"Your current balance for account {account_number} is ${account_currency:,.2f}")  


def make_deposit(account_number: int, amount: float) -> str:
    """
    Returns a string of message about the deposit account.

    Args:
        account_number (int): The account number.
        amount (float): The balance number.

    Returns:
        str: function returns a string message about the deposit amount.

    Raises:
        TypeError: Raised when account number is not an int type.
        ValueError: Raised when account number does not exist, amount not a numberic type, and amount not greater than zero.
    """
        
    if type(account_number) is not int:
        raise TypeError ("Account number must be an int type.")
    elif account_number not in ACCOUNTS:
        raise ValueError ("Account number does not exist.")
    elif type(amount) is str:
        raise ValueError ("Amount must be a numeric type.")
    elif amount <= 0:
        raise ValueError ("Amount must be a value greater than zero.")
    else:
        account_currency = ACCOUNTS[account_number]["balance"]
        amount += account_currency
        ACCOUNTS[account_number]["balance"] = amount
        return (f"You have made a deposit of ${amount:,.2f} to account {account_number}.")

        
def get_task() -> str:
    """
    Returns the task entered by the user in VALID_TASKS.

    Args:
        None

    Returns:
        str: Returns the users input for VALID_TASKS.

    Raises:
        ValueError: Raised when the user inputs an invalid task.
    """

    user_task = input("What would you like to do (balance/deposit/exit)?: ")
    lowercase_string = user_task.lower()

    if lowercase_string not in VALID_TASKS:
        raise ValueError (f" '{user_task}' is an unknown task.")
    else:
        return lowercase_string

# Defines the main implementation of the Chatbot. 
# The implementation of this funtion is INCOMPLETE.
# You will be required to add to this function to make the chatbot work.
def chatbot():

    """
    Returns chat bot for banking tasks using all the functions stated above to loop the task chosen. 
    Users are able to deposit, check balance and quit.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
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