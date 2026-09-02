import input_from_user as iu
import pament_method as pm


if __name__ == "__main__":
    user = iu.user_input()
    customer = user.customer
    bank = user.bank
    account = user.account

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

