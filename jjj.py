total = 0

for i in range(5):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks

average = total / 5

print("Total:", total)
print("Average:", average)

if average >= 50:
    print("Pass")
else:
    print("Fail")
