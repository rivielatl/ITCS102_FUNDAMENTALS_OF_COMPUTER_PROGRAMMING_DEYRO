# Multiple IF AND ELIF CONDITIONS

name = input("Please input your name --> ")
age = int(input("Please input your age --> "))

if age >= 0 and age <= 5:
	print("Your age is considered as INFANT!")
elif age >= 6 and age <= 12:
	print("Your age is considered as KID!")
elif age >= 13 and age <= 15:
	print("Your age is considered as PRE-TEEN!")
elif age >= 16 and age <= 19:
	print("Your age is considered as TEENAGER!")
elif age >= 20 and age <= 29:
	print("Your age is considered as EARLY ADULTHOOD!")
elif age >= 30 and age <= 58:
	print("Your age is considered as ADULT!")
elif age >= 59 and age <= 150:
	print("Your age is considered as SENIOR!")
else:
	print("Your age is INVALID!")

