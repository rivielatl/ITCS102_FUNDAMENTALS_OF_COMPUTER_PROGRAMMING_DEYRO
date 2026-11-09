import getpass

loginattempt = 0

username = "dan"
password = "1234"

while True:
    lusername = input("Username: --> ")
    lpassword = input("Password: --> ")

    if lusername == username and lpassword == password:
        print("Login Successfully...")
        print("Login Attempts: ", loginattempt)
        break
    else:
        print("Login Unsuccessfully...")
        loginattempt = loginattempt + 1
