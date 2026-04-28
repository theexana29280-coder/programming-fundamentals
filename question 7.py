total_units = 0

for i in range(3):
    units = float(input(f"Enter units for month {i+1}: "))
    total_units += units

print("Total Units:", total_units)

if total_units > 300:
    print("High Usage")
else:
    print("Normal Usage")
