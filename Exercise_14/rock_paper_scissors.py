import random

# moves = ['Rock','Paper','Scissors']

# player_1 = input(f'What would you like to choose? {moves} ')
# computer_choice = random.choices(moves)
# print(computer_choice)

choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

player_choice = choices[input("Rock, paper, scissors (R/P/S): ")]
computer_choice = choices[random.choice(list(choices.keys()))]

print(player_choice)
print(computer_choice)

While True()

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


