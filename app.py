from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'


# NOTE: you cannot use this answer in Portfolio Part 2
def check_winner():
    # Winning combinations
    return None


def check_draw():
    return ' ' not in board


@app.route('/')
def index():
    winner = check_winner()
    draw = check_draw()
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if not check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
