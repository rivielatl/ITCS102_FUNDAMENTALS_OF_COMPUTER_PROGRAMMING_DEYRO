# FACTORIAL PROGRAM

def factorial(answer):
    fact = 1
    
    for i in range(answer, 0, -1):
        fact *= answer
        answer -= 1

    return fact

def greet_me(name):
    print("hi " + name) 

def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if x == 0 or y == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
        
if __name__ == "__main__":
    number = int(input("Enter a factorial number: "))
    print(f"Factorial Number: {factorial(number)}")

    namez = input("Enter your name: ")
    greet_me(namez)

    size = int(input("Input your size of box: "))
    print(box(size))
