# While a perching certain item a discount of 10% is offered if the item quantity is more than 1000. If the quantity and the prize 
#of the item is input through the keyboard, write a program to calculate the total cost of the item.

# Taking input from the user
quantity = int(input("Enter the quantity of the item: "))
price = float(input("Enter the price of the item: "))

# Calculating the total cost
total_cost = quantity * price

# Applying discount if quantity is more than 1000
if quantity > 1000:
    total_cost = total_cost - (total_cost * 0.1)

print("The total cost of the item is:", total_cost)