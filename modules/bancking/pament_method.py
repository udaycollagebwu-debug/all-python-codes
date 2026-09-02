class payment_method:
    def __init__(self, method_type, method_fee):
        self.method_type = method_type
        self.method_fee = method_fee

    def payment(self, account, customer, amount=None):
        fee = self.method_fee if amount is None else amount
        method_type = self.method_type

        print("------Status-------")

        if method_type == "debit":
            if account.balance >= fee:
                account.debit(fee)
                print("Debit payment processed.")
                print("Customer account number:", customer.account_number)
                print("Customer name:", customer.name)
                print("Remaining balance:", account.balance)
            else:
                print("Insufficient balance for debit payment.")
                print("Customer account number:", customer.account_number)
                print("Customer name:", customer.name)
                print("Current balance:", account.balance)

        elif method_type == "credit":
            account.credit(fee)
            print("Credit payment processed.")
            print("Customer account number:", customer.account_number)
            print("Customer name:", customer.name)
            print("Remaining balance:", account.balance)

        else:
            print("Unsupported payment method.")

    def pament(self, account, customer, fees=None):
        self.payment(account, customer, amount=fees)
    