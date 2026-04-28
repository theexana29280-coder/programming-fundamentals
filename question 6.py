correct_password = "admin"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Incorrect password")

if attempts == 3:
    print("Account Locked")
