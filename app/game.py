
from random import choice

#
# USER SELECTION
#

def determine_winner(u, c):
    """

    determines the winner of the game

    ex. will determine that the winner, if user chooses rock and computer chooses paper, is the computer

    """
    winners= {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice= winners[u][c]
    return winning_choice
if __name__ == "__main__":

    valid_options = ["rock", "paper", "scissors"]
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner=determine_winner(u, c)

    if winner == u:
        print("You won!")
    elif winner == c:
        print("You lost.")
    elif winner == None:
        print("There's a tie!")