# Global Freight Calculator

Sender_Name = input("Input your name: ")
print("____________________________")
print("A. Utensil Set: ₱250 \nB. Cabinet: ₱750 \nC. Glass Set: ₱850")
print("____________________________")
Type_of_Item = input("Which one do you want to order? (Letter Only) --> ")
itemprice = 0
itemweight = 0
is_fragile = None

print("____________________________")
if Type_of_Item == "A":
  print("The Item you have chosen is: Utensil Set. (₱250)")
  itemprice += 250
  itemweight += 1
  is_fragile = False 
elif Type_of_Item == "B":
  print("The Item you have chosen is: Cabinet. (₱750)")
  itemprice += 750
  itemweight += 4
  is_fragile = False
elif Type_of_Item == "C":
  print("The Item you have chosen is: Glass Set. (₱850)")
  itemprice += 850
  itemweight += 2
  is_fragile = True
else:
  print("Invalid Choice, Please Try Again.")
  exit()

itemamount = eval(input("How many of this item do you want to order? --> "))
itemprice *= itemamount
itemweight *= itemamount
print("Your total cost in your item is: ₱", itemprice)
print("Your total item weight is: ", itemweight, " kg")
print("____________________________")

distance = eval(input(("Input how many kilometers is your distance from seller (number only) --> ")))
print("You are ", distance, " kilometers away from the seller.")
print("____________________________")

is_express = True
is_international = True
International = input("Is your order International? (Yes/No) --> ")

Express = input("Do you need to rush your order? (Yes/No) --> ")

shipping_cost = (itemweight * 2.50) + (distance * 0.15)
total_scost = 0

# This runs when the international and express is true (fragile = true/false)
if International.upper == "YES" and Express.upper == "YES" and is_fragile == True:
    is_express = True
    is_international = True
    total_scost = (shipping_cost * 1.40) + 50 + (itemamount * 15)
elif International.upper == "YES" and Express.upper == "YES" and is_fragile == False:
    is_express = True
    is_international = True
    total_scost = (shipping_cost * 1.40) + 50

# This runs when the international or express is true (only one) also the item weight is less than or equal 20kg (fragile = true/false)
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == True:
    is_express = False
    is_international = True
    total_scost = shipping_cost * 1.20 + (itemamount * 15)
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == True:
    is_express = True
    is_international = False
    total_scost = shipping_cost * 1.20 + (itemamount * 15)
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == False:
    is_express = False
    is_international = True
    total_scost = shipping_cost * 1.20
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == False:
    is_express = True
    is_international = False
    total_scost = shipping_cost * 1.20

# This runs when the international or express is true (only one) also the item weight is more than 20kg (fragile = true/false)
elif International.upper == "YES" and Express.upper == "NO" and itemweight > 20 and is_fragile == True:
    is_express = False
    is_international = True
    total_scost = (shipping_cost * 1.20) + 25 + (itemamount * 15)
elif International.upper == "NO" and Express.upper == "YES" and itemweight > 20 and is_fragile == True:
    is_express = True
    is_international = False
    total_scost = (shipping_cost * 1.20) + 25 + (itemamount * 15)
elif International.upper == "YES" and Express.upper == "NO" and itemweight > 20 and is_fragile == False:
    is_express = False
    is_international = True
    total_scost = (shipping_cost * 1.20) + 25
elif International.upper == "NO" and Express.upper == "YES" and itemweight > 20 and is_fragile == False:
    is_express = True
    is_international = False
    total_scost = (shipping_cost * 1.20) + 25

# This runs when the international or express is true (only one) also the item weight is more than 30kg or 100km distance (fragile = true/false)
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == True and itemweight > 30 or distance >= 100:
    is_express = False
    is_international = True
    total_scost = (shipping_cost * 1.20) + 25 + (itemamount * 15) + 30
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == True and itemweight > 30 or distance >= 100:
    is_express = True
    is_international = False
    total_scost = (shipping_cost * 1.20) + 25 + (itemamount * 15) + 30
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == False and itemweight > 30 or distance >= 100:
    is_express = False
    is_international = True
    total_scost = (shipping_cost * 1.20) + 25 + 30
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == False and itemweight > 30 or distance >= 100:
    is_express = True
    is_international = False
    total_scost = (shipping_cost * 1.20) + 25 + 30

# This runs when the international and express is false and also the distance is less than 2km and distance is less than 100km
elif International.upper == "NO" and Express.upper == "NO" and distance < 2 and distance <= 100:
    total_scost = (shipping_cost * 0)

else:
    print("FAIL")

print("____________________________ \n\n")
print("<-- Your total shopping --> \n Total Item Cost: ", itemprice, "\n Total Shipping Cost: ", total_scost, "\nExpress Order: ", is_express, "\nInternational Order: ", is_international, "\nFragile Item: ", is_fragile)
