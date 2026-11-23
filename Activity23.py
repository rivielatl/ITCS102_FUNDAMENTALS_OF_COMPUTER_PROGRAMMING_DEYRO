# FACTORIAL PROGRAM

number = int(input("Enter a factorial number: "))
def factorial(answer):
    fact = 1
    
    for i in range(answer, 0, -1):
        fact *= answer
        answer -= 1

    return fact

print(f"Factorial Number: {factorial(number)}")
