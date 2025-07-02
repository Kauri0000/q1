#This program will allocate teams randomly from a list of people.
# 1. Import the random module 
# 2. Create a list of people
# 3. Use the random module to randomly allocate teams
# 4. Loop through the list and display each team with its members
# 5. Using an if statement to see if the user is happy with the allocation
# If not, allow them to reallocate teams. If so, the program will end.

import random # Import the random module

# Create a list of players stored in the players variable
players = ["Avery", "Kamari", "Max",
           "Jeffery", "Braylen", "Xavier",
           "Carl", "Walter", "Darren",
           "EJ", "Nahum", "Joaquin",
           "Marshawn", "Ja 'Den", "Isaiah",
           "Kriss", "Joseph", "Semaj",
           "Tay", "Taqari", "Kauri",
           "Kenlon", "Nishad", "Jarmauri"]

def allocateTeams(players): # Create a function
    random.shuffle(players) # Shuffle the list of players
    team1 = players[:len(players) // 2] # Put the first half of the players in team1
    teamCaptain1 = team1 [random.randrange(0, 13)] # Randomly select a team captain from team1
    team2 = players[len(players) // 2:] # Put the second half of the players in team2
    teamCaptain2 = team2 [random.randrange(0, 13)] # Randomly select a team captain from team2

    print("TEAM 1:")
    print ("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)
    print("TEAM 2:")
    print ("Team 2 Captain: " + teamCaptain2)
    for player in team2:
        print(player)

allocateTeams(players)
    