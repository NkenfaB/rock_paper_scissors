import random

print("-----------------------------------------------------------")
print("Welcome to Rock - Paper - Scissors Game!!!")
print("The Rules are simple!")
print("--1.) Rock Beats Scissors --")
print("--2.) Scissors Beats Paper --")
print("--3.) Paper Beats Rock --")
print("The choices are: 'R = Rock', 'P = Paper' or 'S = Scissors' ")
print("Lets Start")
print("-----------------------------------------------------------")

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P, S?: ").upper()
        print("Sorry!! Invaid Input")
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It's a Tie!")
    elif player == "R":
        if computer == "P":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Wins")
        if computer == "S":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player Wins!")
    elif player == "S":
        if computer == "R":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Wins")
        if computer == "P":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player Wins")
    elif player == "P":
        if computer == "S":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Wins")
        if computer == "R":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player Wins")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Come Play Again!")
