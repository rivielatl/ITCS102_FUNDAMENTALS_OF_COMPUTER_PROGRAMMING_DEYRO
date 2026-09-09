# demo
import getpass

print("<---- Register your account ---->")
username = input("Register your username: ")
password = input("Input your password: ")

print("\n----> Log-In System <----")
lusername = input("Username: ")
lpassword = getpass.getpass("Password: ")

if lusername == username and lpassword == password:
	print("\n---> You have successfully LOGGED IN! <---")
	print("Welcome to ACTIVITIY 10! :>")
	print("User: ", username)
else:
	print("\nAccess DENIED!")
	print("Please run the code to try again")
	

