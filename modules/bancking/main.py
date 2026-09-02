import customer_details as cd
import pament_method as pm
import bank_details as bd
import bank_balance as bb


if __name__ == "__main__":
    customer = cd.Customer_details(
        name="Uday",
        age=22,
        address="Ahmedabad",
        phone_number="9876543210",
        account_number="123456789",
        bank_name="State Bank of India",
        acount_type="Savings"
    )

    bank = bd.bank_details(
        bank_name="State Bank of India",
        bank_type="Public Sector",
        bank_address="Ahmedabad, Gujarat",
        bank_phone_number="1800-123-456"
    )

    account = bb.bank_balance(balance=1500)
    while True:
        try:
            amount = float(input("Enter the initial account balance: "))
            if amount < 0:
                raise ValueError("Initial balance cannot be negative.")
            account = bb.bank_balance(balance=amount)
            break
        except ValueError as e:
            print("Invalid input:", e)

    print("===== Customer Details =====")
    customer.display_customer_details()

    print("\n===== Bank Details =====")
    bank.display_bank_details()

    print("\n===== Initial Account Balance =====")
    account.display_balance(customer)

    payment_method = input("\nEnter the payment method (debit/credit): ").strip().lower()
    amount = float(input("Enter the amount for the payment: "))

    if payment_method == "debit":
        payment = pm.payment_method("debit", amount)
    elif payment_method == "credit":
        payment = pm.payment_method("credit", amount)
    else:
        print("Invalid payment method.")
        exit()

    payment.payment(account, customer)