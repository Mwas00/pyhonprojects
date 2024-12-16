# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function to get the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
if discount_percent >= 20:
    print(f"The final price after applying the {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
