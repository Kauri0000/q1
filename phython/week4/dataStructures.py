# 1. Create a list of 5 of your favorite snacks
# 2. Create a tuple of 5 colleges you want to attend
# 3. Create a set of with 5 pieces of data on anything you want; 
# 4. Create a dictionary on a car; key must describe an attribute of the car, followed it's value.
# 5. Once your data structures are created, change a value in all the structures that are mutable. 
# You add, or subtract, or move, data within each structure. 
# (Pay attention to which data structures are mutable. 
# Once done, print all your data structures to the console.

# 1. List of favorite snacks
snacks = ["Chips", "Chocolate", "Cookies", "Popcorn", "Ice Cream"]
snacks += ["Fruit"]  # Adding a new snack


for snack in snacks:
    print(snack)

# 2. Tuple of colleges
colleges = ("Harvard", "Stanford", "MIT", "Yale", "Princeton")
# Nothing because tuples are immutable


for college in colleges:
    print(college)

# 3. Set of data
games = {"Chess", "Soccer", "Basketball", "Tennis", "Baseball"}
games -= {"Soccer"}  # Adding a new game

for game in games:
    print(game)

# 4. Dictionary of a car
carKey = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2025
}
carKey["color"] = "Blue"  # Adding a new attribute
for key in carKey:
    print(carKey.get(key))



