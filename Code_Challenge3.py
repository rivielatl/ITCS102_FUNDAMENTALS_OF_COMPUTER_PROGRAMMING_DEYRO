# Global Freight Calculator

Sender_Name = input("Input your name: ")
print("____________________________")
print("A. Utensil Set: ₱250 \nB. Cabinet: ₱750 \nC. Glass Set: ₱850")
print("____________________________")
Type_of_Item = input("Which one do you want to order? (Letter Only) --> ")

print("____________________________")
if Type_of_Item == "A":
  print("The Item you have chosen is: Utensil Set. (₱250)")
elif Type_of_Item == "B":
  print("The Item you have chosen is: Cabinet. (₱750)")
elif Type_of_Item == "C":
  print("The Item you have chosen is: Glass Set. (₱850)")
else:
  print("Invalid Choice, Please Try Again.")

print("____________________________")
