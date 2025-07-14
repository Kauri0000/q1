#1. A restaurant menu with prices for each item
#2. High scores to an arcade game
#3. All of the months of the year
#4. All the items in your backpack
#5. Look up Student emails by their names
#6. A shopping cart of groceries 
#7. [Add a scenario of your own]

print("Scenario 1: A restaurant menu with prices for each item")
print("Best Structure: Dictionary; best to pair food with price")
menu = {
    "Burger": 8.99,
    "Pizza": 12.99,
    "Salad": 7.49,
    "Soda": 1.99

}

for key, item in menu.items():
    print(key, ":", item)

print("Scenario 2: High scores to an arcade game")
print("Best Structure: List; Need a mutable structure to add scores or update them")
highScores = [
    100,
    105,
    110,
    99

]
for score in highScores:
    print(score)


print("\nScenario 3: All of the months of the year")
print("Best Structure: Tuple; months are fixed and unchangeable")
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)
for month in months:
    print(month)

print("\nScenario 4: All the items in your backpack")
print("Best Structure: List; items can be added or removed")
backPack = [
    "Pencils",
    "Notebook",
    "Water Bottle",
    "Laptop",

]
for item in backPack:
    print(item)

print("\nScenario 5: Look up Student emails by their names")
print("Best Structure: Dictionary; best to pair names with emails")
studentEmails = {
    
}
for name in studentEmails:
    print(name, ":", studentEmails[name])