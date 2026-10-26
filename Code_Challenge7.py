# CODE CHALLENGE 7
# FLOYD'S TRIANGLE

rows = int(input("Input how many rows do you want: "))
counter = 1

for x in range(0, rows, 1):
    for y in range(-1, x):
        print(counter, end=" ")
        counter = counter + 1
    print()
