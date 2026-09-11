# Global Freight Calculator

sender_name = input("Input your name --> ")
type_of_item = input("What type is your item? --> ")
weight = float(input("Enter weight (kg) --> "))
distance = float(input("Enter distance (km) -->  "))
is_express = input("Is it express? (True/False) --> ")
is_international = input("Is it international? (True/False) --> ")
is_fragile = input("Is your item fragile? (True/False) --> ")

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and is_express == False and is_international == False:
    total = 0.00
elif is_international and is_express:
    total = (base_cost * 1.40) + 50
elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total = base_cost + 30
elif fragile == True:
    total = base_cost + 1
else:
    total = base_cost

print("\n_______________________________\n")
print("Sender Name: ", sender_name)
print("Type of Item: ", type_of_item)
print("Shipping Cost: ₱", total)
print("_______________________________")
print("Weight: ", weight, "kg")
print("Distance: ", distance, "km")
print("_______________________________")
print("Is international: ", is_international)
print("Is express: ", is_express)
print("Is fragile: ", is_fragile)
print("\n_______________________________")
