# Global Freight Calculator

Sender_Name = input("Input your name: ")
print("____________________________")
print("A. Utensil Set: ₱250 \nB. Cabinet: ₱750 \nC. Glass Set: ₱850")
print("____________________________")
Type_of_Item = input("Which one do you want to order? (Letter Only) --> ")
itemprice = 0
itemweight = 0
is_fragile = True

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

shipping_cost = 0

if International.upper == "YES" and Express.upper == "YES" and is_fragile == True:
  is_express = True
  is_international = True
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == True:
  is_express = False
  is_international = True
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == True:
  is_express = True
  is_international = False
elif International.upper == "NO" and Express.upper == "NO" and is_fragile == True:
  is_express = False
  is_international = False
elif International.upper == "YES" and Express.upper == "YES" and is_fragile == False:
  is_express = True
  is_international = True
elif International.upper == "YES" and Express.upper == "NO" and is_fragile == False:
  is_express = False
  is_international = True
elif International.upper == "NO" and Express.upper == "YES" and is_fragile == False:
  is_express = True
  is_international = False
elif International.upper == "NO" and Express.upper == "NO" and is_fragile == False:
  is_express = False
  is_international = False
