# ACTIVITY 13 LOAN [CODE CHALLENGE 4 BETTER LOANING]
import getpass

acc_username = "utanganph"
password = "utangna123"

loguser = input("Username: --> ")
logpass = getpass.getpass("Password: --> ")
print("________________________________________________")

if loguser == acc_username and logpass == password:
    firstname = input("What is your first name? --> ")
    jobdescript = input("What is your job? (Include job description if you have job) --> ")
    age = int(input("Enter your age --> "))
    is_employed = bool(input("Are you employed? (True/Leave it Blank) --> "))
    cred_score = eval(input("What is your credit score? (0-1000) --> "))
    annual_income = eval(input("What is your annual income? --> "))
    print("________________________________________________")
    has_collateral = bool(input("Do you have any collateral? (True/Leave it blank) --> "))

    if has_collateral == True:
        print("________________________________________________")
        item_collateral = input("What item is your collateral? --> ")
        value_collateral = eval(input("How much value is your collateral? --> "))

        if value_collateral >= 30000:
            has_collateral = True
        else:
            has_collateral = False
    else:
        item_collateral = "None"

    print("________________________________________________")
    if (age >= 21 and age <= 65) and is_employed == True:
        if cred_score >= 750:
            if annual_income >= 100000:
                inz = 0.045
                inzp = inz * 100
            else:
                inz = 0.05
                inzp = inz * 100
        elif 600 <= cred_score < 750:
            if has_collateral == True:
                inz = 0.07
                inzp = inz * 100
            elif annual_income < 40000:
                inz = 0.095
                inzp = inz * 100
            elif has_collateral == True and annual_income < 40000:
                inz = 0.080
                inzp = inz * 100
            else:
                inz = 0.08
                inzp = inz * 100
        else:
            print("Rejected: Credit score too low.")
            exit()
    else:
        print("Rejected: Fails baseline criteria.")
        exit()
        
    print("________________________________________________\n")
    loan = eval(input("How much do you want to loan? --> "))
    print("\n________________________________________________\n")
    print("First Name: ", firstname)
    print("Money loaned: ₱", loan)
    print("Interest: ", inzp, "%")
    print("Money Interest: ₱", loan * inz)
    print("Loan with Interest: ₱", loan + (loan * inz))
    print("Item Collateral: ", item_collateral)
    print("Value Collateral: ", value_collateral)
else:
    print("Account username/password is incorrect.")

print("________________________________________________")
