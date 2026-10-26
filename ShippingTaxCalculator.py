# Shipping tax calculator

# The price of sale item and destination state from user
item_price = float(input("Enter the price: "))
shipping_state = input("Enter the state: ")

# Find the shipping tax using statements
if shipping_state == "TX" or shipping_state == "LA":
    shipping_tax = 1.25
elif shipping_state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50

# Display the shipping tax
print ("The shipping tax is:", shipping_tax)
