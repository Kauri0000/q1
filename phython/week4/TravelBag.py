#1. Create a list of items in your room you can potentially pack.
#2. Create an empty list to represent your travel bag 
#3. Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
#4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
#5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring

roomItems = ["Clothes", "Snacks", "Macbook", "Toothbrush" ]

print(roomItems)

travelBag = []

# Repeatedly prompt the user for the index of an item to put in their travel bag
for item in roomItems:
    print(item)

item = int(input("item index: "))

while item != 100:
    travelBag.append(roomItems[item])
    roomItems.remove(roomItems[item])
    print("\nYour bedroom:")
    print(roomItems)
    print("\nYour travel bag:")
    print(travelBag)
    item = int(input("item index: "))
    
print("your finsihed")
for item in travelBag:
    print(item)

            
 
