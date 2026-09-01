class CraditCard:
    def __init__(self,coustomer,bank,acnt,limit):
        self.coustomerName = coustomer
        self.bankName = bank
        self.acount = acnt
        self.limit_high = limit
        self.balance = 0.75   # this is the current balence of the coustomear 
    
    def get_costomer(self):
        return self.coustomerName
    def get_bank(self):
        return self.bankName
    def get_acount(self):
        return self.acount
    def get_limit(self):
        return self.limit_high
    def get_ballance(self):
        return self.balance
    
    
    
    def change(self,prize):
        if prize + self.balance > self.limit_high:
            return False
        else:
            self.balance += prize
            return True
    
    def make_pament(self,amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True
    
    def __str__(self):
        return (
            f"Customer: {self.coustomerName}\n"
            f"Bank: {self.bankName}\n"
            f"Account: {self.acount}\n"
            f"Credit Limit: {self.limit_high}\n"
            f"Current Balance: {self.balance}"
        )

if __name__ == '__main__':
    wallet = []
    wallet.append(CraditCard("Uday Sankar Singha","State Bank Of India Saving",'5548 9874 6954 5634',3000))
    wallet.append(CraditCard("Uday Sankar Singha","State Bank Of India Finans",'5674 9987 7654 8765',4000))
    wallet.append(CraditCard("Uday Sankar Singha","State Bank Of India Finens",'9012 9076 2343 0011',5500))

    for val in range(1, 17):
        wallet[0].change(val)
        wallet[1].change(val)
        wallet[2].change(val)

    for card in wallet:
        print(card)
        print("Payment status:", card.make_pament(100))
        print("Updated balance:", card.get_ballance())
        print("-" * 40)