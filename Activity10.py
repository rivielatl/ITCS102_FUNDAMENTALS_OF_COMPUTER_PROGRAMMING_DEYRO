# SELECTION STATEMENT (IF-ELSE)

print("<---- Register your account ---->")
username = input("Register your username: ")
password = input("Input your password: ")

print("\n----> Log-In System <----")
lusername = input("Username: ")

if lusername == username:
	print("Your username is correct! ")
	lpassword = input("Password: ")
	if lpassword == password:
		print("\n-->> You have successfully LOGGED IN! <<--")
		print("Welcome to ACTIVITIY 10! :>")
	else:
		print("Your password is incorrect!")
else:
	print("Your username is incorrect!")

	