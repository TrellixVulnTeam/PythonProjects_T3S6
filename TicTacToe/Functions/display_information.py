from IPython.display import clear_output


def display_board(board):
    clear_output()
    print("Current GAME Status")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
