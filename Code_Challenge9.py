# CODE CHALLENGE 9 

# TASK1
loanamount = 1000
loanyears = 2
rate = 0.00256
remainingloan = loanamount
principal = loanamount / (loanyears * 12)
interest = remainingloan * rate
monthlypayment = interest + principal


print(f"TASK #1 \n \n Enter the loan amount: ${loanamount} \n Enter the loan period in years: {loanyears}")
print("\n Payment Schedule \n Month \t | \t Monthly Payment \t | \t Interest \t | \t Principal \t | \t Remaining Loan")
print("----------------------------------------------------------------------------------------------------------------")

for x in range(1, (12 * loanyears) + 1):
    interest = remainingloan * rate
    monthlypayment = interest + principal
    remainingloan = remainingloan - principal

    
    for y in range(0, 1):
        print(f"{x} \t | \t ${monthlypayment:.2f} \t\t | \t ${interest:.2f} \t\t | \t ${principal:.2f} \t | \t ${remainingloan:.2f}")
    print(end="")

# TASK2
print("\n\n TASK #2 \n\n")

for x in range(0, 7):
    for y in range(0, 13):
        if x == 6 or x+y == 6 or x == y - 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# TASK3
print("\n\n TASK #3 \n\n")

for x in range(0, 5):
    for y in range(0, 5):
        if x == 0 or x == 4 or x+y == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
