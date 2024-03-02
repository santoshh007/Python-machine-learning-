#Create a class for managing a bank account, emphasizing encapsulation with private attributes and methods.
class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    # Setter methods with input validation
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance. Balance must be non-negative.")

    def set_owner(self, owner):
        if owner.strip():
            self.__owner = owner
        else:
            print("Invalid owner name. Owner name cannot be empty.")

    # Method to deposit funds
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    # Method to withdraw funds with input validation
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Successfully withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

# Demonstration
account = BankAccount(account_number="123456789", balance=1000, owner="John Doe")
print("Account Information:")
print("Account Number:", account.get_account_number())
print("Owner:", account.get_owner())
print("Balance:", account.get_balance())

account.deposit(500)
account.withdraw(200)
account.set_owner("Jane Smith")
account.set_balance(1500)

print("\nUpdated Account Information:")
print("Account Number:", account.get_account_number())
print("Owner:", account.get_owner())
print("Balance:", account.get_balance())
