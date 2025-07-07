# Step 1: Create a list of every person at your table
people = ["Kauri", "Marshawn", "Avery", "Max", "Semaj",]



# Step 2: loop through the list and print out each person's name
for person in people:
    print(person)

# Step 3: Prompt the user to print the list again
answer = input("Would you like to see the list of people again? Y/N")
while answer == "Y":
    for person in people:
        print(person)
    answer = input("Would you like to see the list of people again? Y/N") 
    