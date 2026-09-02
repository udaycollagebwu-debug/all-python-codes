class bank_balance:
    def __init__(self, balance=0.0):
        self.balance = balance

    def display_balance(self, customer):
        print("Account Number:", customer.account_number)
        print("Balance:", self.balance)

    def credit(self, amount):
        if amount <= 0:
            raise ValueError("Credit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= 0:
            raise ValueError("Debit amount must be greater than zero.")
        if self.balance < amount:
            return False
        self.balance -= amount
        return True