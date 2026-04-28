total_deposit = 0

while True:
    amount = float(input("Enter deposit amount (0 to stop): Rs. "))
    if amount == 0:
        break
    total_deposit += amount

print(f"Total deposited amount: Rs. {total_deposit:.2f}")

if total_deposit >= 10000:
    print("Premium Customer")
else:
    print("Regular Customer")
