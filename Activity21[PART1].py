# JEEPNEY SIMULATOR USING LISTS

jeepney = []

print(f"> Jeepney has started to move. \nJeepney Passengers: {jeepney}")
jeepney.append("Ana")
print(f"> Ana has ride the Jeepney. \nJeepney Passengers: {jeepney}")
jeepney.append("Ben")
print(f"> Ben has ride the jeepney. \nJeepney Passengers: {jeepney}")
jeepney.append("Carla")
print(f"> Carla has ride the jeepney. \nJeepney Passengers: {jeepney} | Starting with these passengers.")

jeepney.append("Dan")
print(f"\n\n> Dan has ride the jeepney at the back. \nJeepney Passengers: {jeepney}")
jeepney.insert(0, "Lola")
print(f"> Lola has ride the jeepney at the priority seat. \nJeepney Passengers: {jeepney}")
jeepney.remove("Ben")
print(f"> Ben has left in the jeepney [PARA PO!]. \nJeepney Passengers: {jeepney}")
x = jeepney.pop()
print(f"> The last one off by the door. \nJeepney Passenger: {jeepney} \nx is {x}")
y = jeepney.pop(0)
print(f"> The first one off at the front. \nJeepney Passenger: {jeepney} \nx is {x} \ny is {y}")
print(f"How many seats are taken? --> {len(jeepney)}")
print(f"Is Ana still on board? --> {"Ana" in jeepney}")
jeepney.reverse()
print(f"> Return Trip: {jeepney}")


