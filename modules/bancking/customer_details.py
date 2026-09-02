class Customer_details:
    def __init__(self, name, age, address, phone_number, account_number, bank_name, account_type=None, acount_type=None):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.account_number = account_number
        self.bank_name = bank_name
        self.account_type = account_type if account_type is not None else acount_type
        self.acount_type = self.account_type

    def display_customer_details(self):
        print("Customer Name:", self.name)
        print("Customer Age:", self.age)
        print("Customer Address:", self.address)
        print("Customer Phone Number:", self.phone_number)
        print("Customer Account Number:", self.account_number)
        print("Customer Bank Name:", self.bank_name)
        print("Customer Account Type:", self.account_type)