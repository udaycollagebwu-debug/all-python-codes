class user_input:
    def __init__(self):
        self.customer = self.get_customer()
        self.bank = self.get_bank()
        self.account = self.get_account()

    def get_customer(self):
        import customer_details as cd

        customer_name = input("Enter customer name: ")
        customer_age = int(input("Enter customer age: "))
        customer_address = input("Enter customer address: ")
        customer_phone_number = input("Enter customer phone number: ")
        customer_account_number = input("Enter customer account number: ")
        customer_bank_name = input("Enter customer bank name: ")
        customer_account_type = input("Enter customer account type: ")

        return cd.Customer_details(
            name=customer_name,
            age=customer_age,
            address=customer_address,
            phone_number=customer_phone_number,
            account_number=customer_account_number,
            bank_name=customer_bank_name,
            account_type=customer_account_type
        )

    def get_bank(self):
        import bank_details as bd

        bank_name = input("Enter bank name: ")
        bank_type = input("Enter bank type: ")
        bank_address = input("Enter bank address: ")
        bank_phone_number = input("Enter bank phone number: ")

        return bd.bank_details(
            bank_name=bank_name,
            bank_type=bank_type,
            bank_address=bank_address,
            bank_phone_number=bank_phone_number
        )

    def get_account(self):
        import bank_balance as bb

        while True:
            try:
                amount = float(input("Enter the initial account balance: "))
                if amount < 0:
                    raise ValueError("Initial balance cannot be negative.")
                return bb.bank_balance(balance=amount)
            except ValueError as e:
                print("Invalid input:", e)