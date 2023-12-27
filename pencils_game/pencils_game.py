# pencils_game: """The one who is forced to take the last pencil loses"""

import random


def is_winning_position(num_pencils):
    return (num_pencils - 1) % 4 == 0


def bot_move(num_pencils):
    if is_winning_position(num_pencils):
        return random.randint(1, 3)
    else:
        return num_pencils % 4


def start_pencil_game():
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n> "))
            if num_pencils <= 0:
                print("The number of pencils should be positive")
            else:
                break
        except ValueError:
            print("The number of pencils should be numeric")

    while True:
        player1_name = input("Who will be the first (Enter a name): ")
        if player1_name.lower() not in ['john', 'jack']:
            print("Choose between 'John' and 'Jack'")
        else:
            break

    current_player = player1_name
    next_player = 'Jack' if player1_name == 'John' else 'John'

    while num_pencils > 0:
        print("|" * num_pencils)
        print(f"{current_player}'s turn:")

        if current_player == 'Jack':
            pencils_taken = bot_move(num_pencils)
            print(pencils_taken)
        else:
            while True:
                try:
                    pencils_taken = int(input("> "))
                    if pencils_taken < 1 or pencils_taken > 3 or pencils_taken > num_pencils:
                        print("Possible values: '1', '2' or '3'")
                    else:
                        break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        num_pencils -= pencils_taken

        current_player, next_player = next_player, current_player

    print(f"{current_player} won!")


start_pencil_game()
