"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Determine the current player's turn based on the Tic-Tac-Toe board state.

    Args:
    board (list of str): The current state of the Tic-Tac-Toe board. Each element represents a cell
                         on the board and can be 'X', 'O', or ' ' (empty).

    Returns:
    str: The current player's turn ('X' or 'O').
    """
    count_x = sum(1 for cell in board if cell == 'X')
    count_o = sum(1 for cell in board if cell == 'O')

    # X gets the first move, so if X has made fewer moves than O, it's X's turn.
    if count_x <= count_o:
        return 'X'
    else:
        return 'O'

''' Example usage:

initial_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_turn = current_player(initial_board)
print(f"It's {current_turn}'s turn.") 

'''


def actions(board):
    """
    Determine all possible actions that can be taken on the Tic-Tac-Toe board.

    Args:
    board (list of str): The current state of the Tic-Tac-Toe board. Each element represents a cell
                         on the board and can be 'X', 'O', or ' ' (empty).

    Returns:
    set of tuple: A set of all possible actions, where each action is represented as a tuple (i, j).
                  'i' corresponds to the row of the move (0, 1, or 2), and 'j' corresponds to which cell
                  in the row corresponds to the move (0, 1, or 2).
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                possible_actions.add((i, j))

    return possible_actions

''' Example usage:

initial_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', 'X', ' ']
]
possible_moves = actions(initial_board)
print("Possible Moves:", possible_moves)

'''


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
