# Build a rock-paper-scissors game
# 0. Ask the players for their names
# 1. Prompt player 1 for RPS
# 2. Prompt player 2 for RPS
# 3. Compare p1 and p2 choices and decide a winner

def RPS():
    print("Welcome to Rock, Paper, Scissors")
    # Ask for player names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    # Ask players for their choices
    p1_Choice = input(f"{player1}, please choose Rock, Paper, or Scissors: ").lower()
    while not IsValidMove(p1_Choice):
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        p1_Choice = input(f"{player1}, please choose Rock, Paper, or Scissors: ")

    p2_Choice = input(f"{player2}, please choose Rock, Paper, or Scissors: ").lower()
    while not IsValidMove(p2_Choice):
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        p2_Choice = input(f"{player2}, please choose Rock, Paper, or Scissors: ")

    # Compare Player moves
    if p1_Choice == p2_Choice:
        print("It's a tie!")
    
    if p1_Choice == "rock" and p2_Choice == "scissors": 
        print(f"Rock beats Scissors, {player1} wins!")
    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"Paper beats Rock, {player1} wins!")
    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"Scissors beats Paper, {player1} wins!")
    elif p2_Choice == "rock" and p1_Choice == "scissors":
        print(f"Rock beats Scissors, {player2} wins!")
    elif p2_Choice == "paper" and p1_Choice == "rock":
        print(f"Paper beats Rock, {player2} wins!")
    elif p2_Choice == "scissors" and p1_Choice == "paper":
        print(f"Scissors beats Paper, {player2} wins!")
   
def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]
    
    if playerMove in validMoves:
        return True
    else:
        return False



RPS()

