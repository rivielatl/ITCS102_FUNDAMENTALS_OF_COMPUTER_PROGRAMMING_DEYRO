# BOX

column = 7
rows = 9
for x in range(column):
    for y in range(rows):
        if x == 0 or y == 0 or x == 6 or y == 8:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
