import random
from random import randint

print("Welcome to Siris's Tic Tac Toe\n")
print("Player 1 is O. Player 2 is X.\n")

board_selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board(board_selection):
    print(f" {board_selection[0]} | {board_selection[1]} | {board_selection[2]}")
    print("-----------")
    print(f" {board_selection[3]} | {board_selection[4]} | {board_selection[5]}")
    print("-----------")
    print(f" {board_selection[6]} | {board_selection[7]} | {board_selection[8]}")

print_board(board_selection)


print("\nA coin is flipped.")
coin_result = random.randint(0,1)
if coin_result == 0:
    current_player = "Player1"
    print(f"\nThe coin landed on heads! The human P1 goes first.")


def player1_turn(board_selection):
    while True:
        player1_choice = input("Please choose which number you want to place your O (between 1-9): ")
        if player1_choice.isdigit() and int(player1_choice) in range(1,10):
            index_spot_chosen = int(player1_choice) - 1 #converts number chosen to index on board grid
            if board_selection[index_spot_chosen] not in ['X', 'O']:
                board_selection[index_spot_chosen] = 'O'
                break  #breaks after a valid move
            else:
                print("That spot is already taken. Please select a different spot.")
        else:
            print("You must choose a number between 1-9.")

def player2_turn(board_selection):
    while True:
        player2_turn() = random.randint(1, 9)
        index_spot_chosen = int(player1_choice) - 1  # converts number chosen to index on board grid
        if board_selection[index_spot_chosen] not in ['X', 'O']:
            board_selection[index_spot_chosen] = 'X'
            break  # breaks after a valid move


if coin_result == 0:
    current_player = "Player1"
    print(f"\nThe coin landed on heads! The human goes first.")
    player_1st_choice = input("Please choose which number you want to place your O (between 1-9): ")
    print(f"You chose spot number: {player_1st_choice}\n")
    index_spot_chosen = int(player_1st_choice) - 1
    board_selection[index_spot_chosen] = 'O'
    print_board(board_selection)
else:
    current_player = "Player2"
    print(f"\nThe coin landed on tails! 2nd player goes first.")
    print("The computer will place it's X on a spot.")
    computer_turn_1 = random.randint(1,10)
    print(f"The computer chose spot number: {computer_turn_1}\n")
    index_spot_chosen = int(computer_turn_1) - 1
    board_selection[index_spot_chosen] = 'X'
    print_board(board_selection)


while True:
    if current_player == "Player1":



# # player's turn
# Hit_or_Stay = input(f"Do you want to Hit or Stay? (H or S): ").upper()
# if Hit_or_Stay != "H":
#     break
#
# # computer's turn (only if the player hasn't busted)
# if not player_busted:
#     computer_points_counter = 0
#     computer_continue_playing = True
#     while computer_continue_playing:
#         print("The dealer flips over their next card")
#         time.sleep(1.5)
#         drawn_random_card = random.randint(2, 14)
#
#         if drawn_random_card == 1 or drawn_random_card == 11:
#             face_card = "Ace"
#             True_point_value = 11
#             print(f"It drew an Ace. That's {True_point_value} points!")
#             computer_points_counter += True_point_value
#
#         elif 2 <= drawn_random_card <= 10:
#             print(f"It got dealt a {drawn_random_card}")
#             computer_points_counter += drawn_random_card
#
#         elif drawn_random_card == 12:
#             face_card = "Jack"
#             print(f"It got dealt a {face_card}")
#             computer_points_counter += 10
#
#         elif drawn_random_card == 13:
#             face_card = "Queen"
#             print(f"It got dealt a {face_card}")
#             computer_points_counter += 10
#
#         elif drawn_random_card == 14:
#             face_card = "King"
#             print(f"It got dealt a {face_card}")
#             computer_points_counter += 10
#
#         if computer_points_counter >= 22:
#             print("Computer went over! You win!")
#             computer_continue_playing = False
#         elif computer_points_counter >= 17:
#             print(f"The dealer Stays at {computer_points_counter} points")
#             computer_continue_playing = False
#             if computer_points_counter > points_counter:
#                 print(f"The dealer beat you with {computer_points_counter} points to your {points_counter}.")
#             elif computer_points_counter == points_counter:
#                 print("It's a draw!")
