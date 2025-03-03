class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"  

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

    def check_balance(self):
        print(f"Current Balance: {self.balance}")
    
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example usage:
account = BankAccount("123456", "Nestah", 5000, "2025-03-01")
print(account.deposit(1000))
print(account.withdraw(3000))
account.check_balance()
account.customer_details()
