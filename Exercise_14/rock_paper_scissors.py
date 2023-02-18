# We have imported the Random Module
import random


# while loop to extend game and allow player to end the game or keep playing an infinite amount of times
while True:

# gives user choice to play a move
# created a dictionary of choices for user
# prompts the user to enter a value of: R, P, S and converts the value into Rock, Paper or Scissors

    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    player_choice = choices[input("Rock, paper, scissors (R/P/S): ")]

# Ask the computer to generate a random value between 0 and 2 and converts the computer's choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
# Computer player can randomly select a move from choices 0 to 2
    computer_choice = choices[random.choice(list(choices.keys()))]
    print(f'You have selected {player_choice} and your opponent has picked {computer_choice}')

# Conditional statements to decide winner of game
# Compares the user's choice with computer's choice to display a message indicating whether user won, lost or drew against computer
    if player_choice == computer_choice:
        print(f'You have both selected {player_choice}. You are tied!')
    elif computer_choice == 'Rock' and player_choice == 'Scissors':
        print('Rock smashes Scissors, You lose!')
    elif computer_choice == 'Scissors' and player_choice == 'Paper':
        print('Scissors cut paper! You lose!')
    elif computer_choice == 'Paper' and player_choice == 'Rock':
        print('Paper wraps rock. You lose!')
    else:
        print('You have won!')

# Asks the player if they want to replay or leave the game
    player_replay = input('Would you like to replay? y/n ')
    if player_replay != 'y':
        print('You have chosen to not play again. Goodbye!')
        break
