import random 

print("Welcome to Rock Paper Scissors Game")

options = ["rock","paper","scissors"] 

computer_wins = 0 
user_wins = 0
no_of_ties = 0

while True:
    user_choice = input("Type Rock/Paper/Scissors or q ").lower()
    print(user_choice)
    if user_choice not in options:
        break 
    computer_choice = random.choice(options) 
    print(computer_choice)
    if user_choice != computer_choice:
        if user_choice == "rock" and computer_choice=="scissors":
            print("You Won!")
            user_wins += 1 
        elif user_choice == "paper" and computer_choice == "rock":
            print("You Won!")
            user_wins += 1 
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You Won!")
            user_wins += 1 
        else:
            print("You Lost!")
            computer_wins += 1 
    else:
        print("Game Tied!!!")
        no_of_ties += 1
print("user wins",user_wins,"times.")
print("computer wins",computer_wins,"times.")
print("Game Tied",no_of_ties,"times.")
print("Good Bye!")

