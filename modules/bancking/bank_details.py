class bank_details:
    def __init__(self,bank_name,bank_type,bank_address,bank_phone_number):
        self.bank_name = bank_name
        self.bank_type = bank_type
        self.bank_address = bank_address
        self.bank_phone_number = bank_phone_number
        
    def display_bank_details(self):
        print("Bank Name:", self.bank_name)
        print("Bank Type:", self.bank_type)
        print("Bank Address:", self.bank_address)
        print("Bank Phone Number:", self.bank_phone_number)