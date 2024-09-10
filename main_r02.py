import random

print("Welcome to Siris's Tic Tac Toe\n")
print("Player 1 is O. Player 2 is X.\n")

# Initial board setup
board_selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to print the board
def print_board(board_selection):
    print(f" {board_selection[0]} | {board_selection[1]} | {board_selection[2]}")
    print("-----------")
    print(f" {board_selection[3]} | {board_selection[4]} | {board_selection[5]}")
    print("-----------")
    print(f" {board_selection[6]} | {board_selection[7]} | {board_selection[8]}")

print_board(board_selection)

# Coin flip to decide who goes first
print("\nA coin is flipped.")
coin_result = random.randint(0, 1)
if coin_result == 0:
    current_player = "Player1"
    print(f"\nThe coin landed on heads! Player 1 'O' goes first.")
else:
    current_player = "Player2"
    print(f"\nThe coin landed on tails! Player 2 'X' goes first.")

# Function for Player 1's (human) turn
def player1_turn(board_selection):
    while True:
        player1_choice = input("Please choose which number you want to place your O (between 1-9): ")
        if player1_choice.isdigit() and int(player1_choice) in range(1, 10):
            index_spot_chosen = int(player1_choice) - 1  # Convert chosen number to board index
            if board_selection[index_spot_chosen] not in ['X', 'O']:
                board_selection[index_spot_chosen] = 'O'
                break  # Break out of the loop after a valid move
            else:
                print("That spot is already taken. Please select a different spot.")
        else:
            print("You must choose a number between 1-9.")

# Function for Player 2's (computer) turn
def player2_turn(board_selection):
    while True:
        computer_choice = random.randint(1, 9)
        index_spot_chosen = computer_choice - 1  # Convert computer's choice to board index
        if board_selection[index_spot_chosen] not in ['X', 'O']:
            board_selection[index_spot_chosen] = 'X'
            print(f"The computer placed its X on spot {computer_choice}")
            break  # Break after a valid move

# main game loop:
while True:
    if current_player == "Player1":
        player1_turn(board_selection)
        print_board(board_selection)
        current_player = "Player2"
    else:
        # current_player == "Player2":
        player2_turn(board_selection)
        print_board(board_selection)
        current_player = "Player1"