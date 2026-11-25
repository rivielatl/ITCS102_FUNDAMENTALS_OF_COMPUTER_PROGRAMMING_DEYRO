from activity23 import factorial, greet_me, box
import os

while True:
    question = input(f"SELECT AN OPTION: \n --> [1] Factorial \n --> [2] Greet_Me \n --> [3] Box \n --> [4] Quit \n >> ")

    if question == "1":
        os.system('cls')
        print("OUTPUT:  ----->")
        number = int(input("Enter a factorial number: "))
        print(f"Factorial Number: {factorial(number)}")
    elif question == "2":
        os.system('cls')
        print("OUTPUT:  ----->")
        namez = input("Enter your name: ")
        greet_me(namez)
    elif question == "3":
        os.system('cls')
        print("OUTPUT:  ----->")
        size = int(input("Input your size of box: "))
        print(box(size))
    elif question == "4":
        os.system('cls')
        break
    else:
        print("Error: The choice you have picked isn't included.")
