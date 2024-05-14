calculate_discount = ()

price = float(input("Enter the original price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

calculate_discount = price * (discount_percent / 100)

if discount_percent > 20:
    result = calculate_discount
else:
    result = price
