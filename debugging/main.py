#Jonas Fairchild, fix the game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 1 #Set this to 1 since it would previously allow you to have 11 attempts. Logic error. It made the game give you an extra turn when it shouldn't have.
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #This wasn't converted to an integer, so the program couldn't take it. Syntax error. This made it so that none of the conditional statements could detect if their condition was met.
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1 #The 'attempts' value was not being incremented, so the lose condition would never be met. Logic error. This made it so that the game would give you infinite tries, even though it should only give you 10.
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        continue
    print("Game Over. Thanks for playing!")
start_game()