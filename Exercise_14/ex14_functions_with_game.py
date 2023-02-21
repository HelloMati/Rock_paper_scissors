import exercise_14_functions
# We have imported the Random Module

# Welcome message to user using a function

exercise_14_functions.welcome()

# while loop to extend game and allow player to end the game or keep playing an infinite amount of times

while True:

# gives user choice to play a move
# created a dictionary of choices for user
# prompts the user to enter a value of: R, P, S and converts the value into Rock, Paper or Scissors

    user, computer = exercise_14_functions.choose_moves()

# Conditional statements to decide winner of game
# Compares the user's choice with computer's choice to display a message indicating whether user won, lost or drew against computer
    exercise_14_functions.decide_winner(user, computer)

# Asks the player if they want to replay or leave the game- used a function
    player_replay = input('Would you like to replay? y/n ')
    if player_replay != 'y':
        exercise_14_functions.exit_game()
        break
