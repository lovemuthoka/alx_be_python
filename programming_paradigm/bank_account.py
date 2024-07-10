class BankAccount:
    def __init__(self, initial_balance=0):
        
        self.account_balance = initial_balance

    def deposit(self, amount):
        
        self.account_balance += amount

    def withdraw(self, amount):

        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        
        print(f"Current balance: ${self.account_balance:.2f})

 account = BankAccount(100)  # Create an account with an initial balance of $100
account.display_balance()  # Output: Current balance: $100.00

account.deposit(50)  # Deposit $50
account.display_balance()  # Output: Current balance: $150.00

account.withdraw(20)  # Withdraw $20
account.display_balance()  # Output: Current balance: $130.00

account.withdraw(150)  # Attempt to withdraw $150 (insufficient funds)
print(account.withdraw(150))  # Output: False
account.display_balance()  # Output: Current balance: $130.00
