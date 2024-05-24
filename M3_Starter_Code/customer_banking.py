# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: The updated savings account balance after adding the interest earned and the interest earned itself.
    """
    savings_account = Account(balance, 0)  # Create an instance of the Account class for savings
    interest_earned = (balance * interest_rate * months) / 12
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)  # Use set_balance method to update balance
    savings_account.set_interest(interest_earned)  # Use set_interest method to update interest
    return updated_balance, interest_earned

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: The updated CD account balance after adding the interest earned and the interest earned itself.
    """
    cd_account = Account(balance, 0)  # Create an instance of the Account class for CD account
    interest_earned = (balance * interest_rate * months) / 12
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)  # Use set_balance method to update balance
    cd_account.set_interest(interest_earned)  # Use set_interest method to update interest
    return updated_balance, interest_earned

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_balance = float(input("Enter your savings account balance: \n"))
    savings_interest = float(input("Enter your savings account interest rate (APR): \n"))
    savings_maturity = int(input("Enter the months for your savings account maturity: \n"))
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Savings Account Interest Earned: ${interest_earned_savings:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    cd_balance = float(input("\nEnter your CD account balance: \n"))
    cd_interest = float(input("Enter your CD account interest rate (APR): \n"))
    cd_maturity = int(input("Enter the months for your CD account: \n"))
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"\nCD Account Interest Earned: ${interest_earned_cd:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()