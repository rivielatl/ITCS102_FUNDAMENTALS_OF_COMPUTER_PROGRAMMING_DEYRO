# FACTORIAL PROGRAM

number = int(input("Enter a factorial number: "))
def factorial(answer):
    fact = 1
    
    for i in range(answer, 0, -1):
        fact *= answer
        answer -= 1

    return fact

print(f"Factorial Number: {factorial(number)}")

namez = input("Enter your name: ")
def greet_me(name):
    print("hi " + name)
    
greet_me(namez)

size = int(input("Input your size of box: "))
def box(sizes):
    for x in range(sizes+1):
        for y in range(sizes+1):
            if x == 0 or y == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    return sizes
        
print(box(size))
