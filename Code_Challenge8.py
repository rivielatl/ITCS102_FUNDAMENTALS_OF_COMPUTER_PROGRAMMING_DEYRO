# CODE CHALLENGE 8 
# DIAMOND W/ SPACES


# MANUAL

# MANUAL
rows = 7

for x in range(0, rows):
    for y in range(0, rows):
        if x+y == 3 or x+y == 9 or (y != 5 and x+y == 5 and x != 5) or (y != 6 and x+y == 7 and x != 6):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
print("\n=======\n")

# AUTOMATIC
rows = int(input("Enter how many rows: "))

for x in range(rows):
  for y in range(rows - x - 1):
    print(" ", end="")
  for z in range(x+1):
    print("* ", end="")
  print()

for x in range(rows):
  for y in range(x+1):
    print(" ", end="")
  for z in range(rows - x - 1):
    print("* ", end="")
  print()