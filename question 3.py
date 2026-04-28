total = 0
for i in range(1, 6):
    price = float(input(f"Enter price of item {i}: Rs. "))
    total += price

discount = 0
if total > 5000:
    discount = total * 0.20

final_amount = total - discount

print(f"\nTotal amount: Rs. {total:.2f}")
print(f"Discount applied: Rs. {discount:.2f}")
print(f"Final payable amount: Rs. {final_amount:.2f}"
