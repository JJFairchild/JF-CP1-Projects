#Jonas Fairchild, Rock, Paper, Scissors

import random #This part of the code just defines necessary lists and values, and greets the player.
print("This program will let you play Rock, Paper, Scissors against the computer. Make sure to capitalize your input, and have fun!")
rps = ["Rock", "Paper", "Scissors"]
playerscore = 0
botscore = 0

while True:
    
    player = input("What would you like to play?: ") #This code gets an input from the player, Rock, Paper, or Scissors.
    while not player in rps:
        print("Unrecognizable input. Try again.")
        player = input("What would you like to play?: ")
    print(f"Player: {player}")
    
    bot = rps[random.randint(0, 2)] #This gets a random value, Rock, Paper, or Scissors.
    print(f"Computer: {bot}")

    if player == bot: #This code checks for a winner and displays it. Also adds score accordingly.
        print("That's a tie!")
    elif player == "Rock":
        if bot == "Paper":
            print("Paper covers rock. Computer wins!")
            botscore += 1
        elif bot == "Scissors":
            print("Rock smashes scissors. Player wins!")
            playerscore += 1
    elif player == "Paper":
        if bot == "Rock":
            print("Paper covers rock. Player wins!")
            playerscore += 1
        elif bot == "Scissors":
            print("Scissors cut paper. Computer wins!")
            botscore += 1
    elif player == "Scissors":
        if bot == "Rock":
            print("Rock smashes scissors. Computer wins!")
            botscore += 1
        elif bot == "Paper":
            print("Scissors cut paper. Player wins!")
            playerscore += 1

    print(f"Score: {playerscore}:{botscore}") #Prints the score
    
    keep_playing = input("Would you like to keep playing?: ") #Asks the user if they want to keep playing and displays a final score if not.
    while keep_playing != "Yes":
        if keep_playing == "No":
            print("Goodbye. thanks for playing!")
            print(f"Final score: {playerscore}:{botscore}")
            break
        elif keep_playing != "Yes":
            print("Unrecognizable input. Try again.")
        keep_playing = input("Would you like to keep playing?: ")