# ACTIVITY 13 LOAN

age = int(input("Enter your age --> "))
is_employed = bool(input("Are you employed? (True/Leave it Blank) --> "))
cred_score = eval(input("What is your credit score? (0-1000) --> "))
annual_income = eval(input("What is your annual income? --> "))
print("________________________________________________")
has_collateral = bool(input("Do you have any collateral? (True/Leave it blank) --> "))

if has_collateral == True:
    item_collateral = input("What item is your collateral? --> ")
else:
    item_collateral = "None"

print("________________________________________________")
if (age >= 21 and age <= 75) and is_employed == True:
    if cred_score >= 750:
        if annual_income >= 100000:
            inz = 4.5
        else:
            inz = 5.0
    elif 600 <= cred_score < 750:
        if has_collateral == True:
            inz = 7.0
        elif annual_income < 40000:
            inz = 9.5
        elif has_collateral == True and annual_income < 40000:
            inz = 8.0
        else:
            inz = 8.0
    else:
        print("Rejected: Credit score too low.")
        exit()
else:
    print("Rejected: Fails baseline criteria.")
    exit()
    
print("________________________________________________\n")
loan = eval(input("How much do you want to loan? --> "))
print("\n________________________________________________\n")
print("Money loaned: ₱", loan)
print("Interest: ", inz, "%")
print("Loan with Interest: ₱", loan * inz)
print("Item Collateral: ", item_collateral)
