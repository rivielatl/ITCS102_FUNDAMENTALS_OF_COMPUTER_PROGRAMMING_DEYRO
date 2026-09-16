# ACTIVITY 13 LOAN

age = int(input("Enter your age --> "))
is_employed = bool(input("Are you employed? (True/Leave it Blank) --> "))
cred_score = eval(input("What is your credit score? (0-1000) --> "))
annual_income = eval(input("What is your annual income? --> "))
print("________________________________________________")
has_collateral = bool(input("Do you have any collateral? (True/Leave it blank) --> "))

print("________________________________________________")
if (age >= 21 and is_employed == True:
    if cred_score >= 750:
        if annual_income >= 100000:
            inz = 0.045
        else:
            inz = 0.05
    elif 600 <= cred_score < 750:
        if has_collateral == True:
            inz = 0.07
        elif annual_income < 40000:
            inz = 0.095
        elif has_collateral == True and annual_income < 40000:
            inz = 0.080
        else:
            inz = 0.08
    else:
        print("Rejected: Credit score too low.")
        exit()
else:
    print("Rejected: Fails baseline criteria.")
    exit()
    
print("Interest: ", inz, "%")
