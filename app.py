from flask import Flask, render_template, redirect, url_for
from score import get_scores, update_scores, reset_scores

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'


# NOTE: you cannot use this answer in Portfolio Part 2
def check_winner():
    # Winning combinations (row, column, diagonal)
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle Row
        [6, 7, 8],  # Bottem Row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Left column
        [2, 4, 6],  # Right diagonal
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return current_player  # Return the current player as a winner.

    return None


def check_draw():
    return ' ' not in board


@app.route('/')
def index():
    winner = check_winner()
    draw = check_draw()
    scores = get_scores()
    return render_template('index.html',
                           board=board,
                           current_player=current_player,
                           winner=winner,
                           draw=draw,
                           scores=scores)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if check_winner():
            update_scores('Player 1' if current_player == 'X' else 'Player 2')
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    reset_scores()  # Reset the scores when resetting the game
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
