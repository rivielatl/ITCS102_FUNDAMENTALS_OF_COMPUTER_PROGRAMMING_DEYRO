# JEEPNEY SIMULATOR (INTERACTIVE)

route = ["Grand Terminal", "SM Lucena City", "Perez Park", "Pacific Mall", "Ibabang Iyam"]
passengers = []
seats = 18
fare = 14
discount = 0.07
total = 0

while True:
    print("===============================")
    print(f"--> Sakay: {passengers}")
    print(f"--> {len(passengers)} of {seats} Seats.")
    print(f"Options: \n1. Sakay \n2. Priority Seat \n3. Para po! \n4. Baba sa pinto \n5. Baba sa harap\n6. Seat check \n7. Balikan \n8. Exit")
    print("===============================")

    choice = input("Choice: ")
    
    if choice == "1":
        if len(passengers) == seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(f"{name}, boarded at the back.")
    
    elif choice == "2":
        if len(passengers) == seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + (fare * discount)
            print(f"{name}, took the priority seat.")
    
    elif choice == "3":
        name = input("Who is getting off? --> ")
        if name in passengers:
            passengers.remove(name)
            print(f"{name}, got off. Ingat!")
    
    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(f"{left}, got off at the door.")
            
    elif choice == "5":
        if len(passengers) == 0:
                    print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(f"{left}, got off at the front.")
    
    elif choice == "6":
        for i in range(len(passengers)):
            print(f"Seat: {i + 1, passengers[i]}")
    
    elif choice == "7":
        route.reverse()
        print(f"Route: {route}")
    
    elif choice == "8":
        print(f"Total Fare Today: {total}")
        break
    
    else:
        print("Invalid Choice.")
