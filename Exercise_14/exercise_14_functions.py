import random
# Functions for game


def welcome():
    user_name= input('Please enter your name: ')
    print(f'Welcome to the game {user_name}!')


def exit_game():
    print('Thank you for playing. Goodbye!')


def decide_winner(player_choice, computer_choice):
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


def choose_moves():
    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    player_choice = choices[input("Rock, paper, scissors (R/P/S): ").upper()]
    computer_choice = choices[random.choice(list(choices.keys()))]
    print(f'You have selected {player_choice} and your opponent has picked {computer_choice}')
    return player_choice, computer_choice
