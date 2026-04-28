low_stock_count = 0

for i in range(1, 6):
    stock = int(input(f"Enter stock quantity for product {i}: "))
    if stock < 10:
        low_stock_count += 1

print(f"Number of products low in stock: {low_stock_count}")
