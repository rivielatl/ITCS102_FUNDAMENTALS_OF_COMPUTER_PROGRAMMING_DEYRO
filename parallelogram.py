# PARALLELOGRAM

rows = 7

for x in range(rows):
    for y in range(rows+1):
        if x + y == 3:
            print("* ", end="")
        elif (y != 5 and x == 3 and y != 6 and y != 7) or (y != 2 and y != 0 and x == 0 and y != 1):
            print("* ", end="")
        elif (y == 7 and x < 3 and x != 1):
            print(" *", end="")
        elif (y == 7 and x < 2):
            print("  *", end="")
        else:
            print(" ", end="")
    print()
