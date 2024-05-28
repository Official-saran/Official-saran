marked_price = float(input("Enter the marked price: \n"))
if marked_price > 10000:
    discount = 0.20
elif marked_price > 7000:
    discount = 0.15
else:
    discount = 0.10
net_amount = marked_price - (discount * marked_price)
print(f"The net amount to pay after discount is: {net_amount:.2f}")
