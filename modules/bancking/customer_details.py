class Customer_details:
    def __init__(self, name, age, address, phone_number, account_number,bank_name,acount_type):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.account_number = account_number
        self.bank_name = bank_name
        self.acount_type = acount_type
    
    def display_customer_details(self):
        print("Customer Name:", self.name)
        print("Customer Age:", self.age)
        print("Customer Address:", self.address)
        print("Customer Phone Number:", self.phone_number)
        print("Customer Account Number:", self.account_number)
        print("Customer Bank Name:", self.bank_name)
        print("Customer Account Type:", self.acount_type)