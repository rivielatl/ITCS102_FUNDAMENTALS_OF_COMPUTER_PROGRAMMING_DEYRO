# CODE CHALLENGE 6
# THE X 

rows = int(input("Input how many rows do you want: "))


for x in range(0, rows):
    for y in range(0, rows):
        if x == y or x+y == rows-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
