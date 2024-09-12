player1_score = 0
player2_score = 0

print("hello")


def get_scores():
    """
    Return the current scores as a dictionary.
    This can be used to access scores outside of this file.
    :return:
    """
    return {'Player 1': player1_score, 'Player 2': player2_score}


def update_scores(winner):
    """
    Update the score based on the winner.

    Parameters:
    winner (str): The name of the player who won ('Player 1' or 'Player 2').
    """
    global player1_score, player2_score
    if winner == 'Player 1':
        player1_score += 1
    elif winner == 'Player 2':
        player2_score += 1


def display_scores():
    """
    Print the current scores to the console.
    """
    print(f"Player 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")


def reset_scores():
    """
    Reset both player's scores to zero.
    This can be called to start a fresh game.
    """
    global player1_score, player2_score
    player1_score = 0
    player2_score = 0
