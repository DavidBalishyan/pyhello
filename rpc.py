# Rock, Paper, Scissors game in python
import random

options = (
    "rock",
    "paper",
    "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("rock, paper, or scissors? ").lower()

if player == computer:    
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print(f"You lose! ::: Computer: {computer}")
    elif computer == "scissors":
        print(f"You win! ::: Computer: {computer}")
elif player == "paper":
    if computer == "scissors":
        print(f"You lose! ::: Computer: {computer}")
    elif computer == "rock":
        print(f"You win! ::: Computer: {computer}")
elif player == "scissors":
    if computer == "rock":
        print(f"You lose! ::: Computer: {computer}")
    elif computer == "paper":
        print(f"You win! ::: Computer: {computer}")
else:
    print("That's not a valid play. Check your spelling!")