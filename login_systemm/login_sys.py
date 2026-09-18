correct_username = "admin"
correct_password = "1234"
attempt = 0
while attempt < 3:
    user=input("please enter username: ")
    password = input("please enter password: ")
    if user == correct_username and password == correct_password:
        print("login successful")
        break
    print("wrong username or password")
    attempt += 1
else:
    print("account locked! too many attempts")
