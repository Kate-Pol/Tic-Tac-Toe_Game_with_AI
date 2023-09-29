"""
Tic Tac Toe Player
"""

import math
import copy

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

def is_valid_action(board, action):
    """
    Check if the given action is valid for the current board.

    Args:
    board (list of list): The current state of the Tic-Tac-Toe board.
    action (tuple): The action to check, represented as a tuple (row, col).

    Returns:
    bool: True if the action is valid, False otherwise.
    """
    row, col = action
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        return True
    return False

def result(board, action, player):
    """
    Get the result of applying the given action to the current board for a specific player.

    Args:
    board (list of list): The current state of the Tic-Tac-Toe board.
    action (tuple): The action to apply, represented as a tuple (row, col).
    player (str): The player making the move ('X' or 'O').

    Returns:
    list of list: The new board state after applying the action.
    
    Raises:
    ValueError: If the action is not valid for the current board.
    """
    
    if not is_valid_action(board, action):
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)  # Create a deep copy to keep the original board intact
    row, col = action
    new_board[row][col] = player  # Apply the player's move to the new board
    return new_board


def winner(board):
    """
    Determine the winner of the Tic-Tac-Toe game.

    Args:
    board (list of list): The current state of the Tic-Tac-Toe board.

    Returns:
    str or None: The winner ('X' or 'O') if there is one, or None if there is no winner.
    """
    
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None  # No winner found

''' Example usage:

current_board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', ' ']
]
result = winner(current_board)
print("Winner:", result)

'''

def terminal(board):
    """
    Determine if the Tic-Tac-Toe game is over.

    Args:
    board (list of list): The current state of the Tic-Tac-Toe board.

    Returns:
    bool: True if the game is over, False if it is still in progress.
    """
    
    # Check if there is a winner
    winner_player = winner(board)
    if winner_player:
        return True  # Game is over, there's a winner

    # Check if all cells are filled
    for row in board:
        if ' ' in row:
            return False  # Game is still in progress, at least one empty cell

    return True  # Game is over, it's a tie (all cells filled, but no winner)

''' Example usage:
current_board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]
result = terminal(current_board)
print("Game Over:", result)
'''

def utility(board):
    """
    Calculate the utility (score) of the terminal Tic-Tac-Toe board.

    Args:
    board (list of list): The terminal state of the Tic-Tac-Toe board.

    Returns:
    int: The utility of the board (1 for 'X' win, -1 for 'O' win, 0 for a tie).
    """
    
    winner_player = winner(board)

    if winner_player == 'X':
        return 1  # 'X' has won, utility is 1
    elif winner_player == 'O':
        return -1  # 'O' has won, utility is -1
    else:
        return 0  # It's a tie, utility is 0

''' Example usage:
terminal_board_x_win = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]
result = utility(terminal_board_x_win)
print("Utility:", result)
'''

def minimax(board):
    """
    Determine the optimal move for the player whose turn it is on the Tic-Tac-Toe board.

    Args:
    board (list of list): The current state of the Tic-Tac-Toe board.

    Returns:
    tuple or None: The optimal move as a tuple (i, j), or None if the board is terminal.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)

        v = float('-inf')
        best_move = None

        for action in actions(board):
            min_result = min_value(result(board, action, 'X'))
            if min_result > v:
                v = min_result
                best_move = action

        return best_move

    def min_value(board):
        if terminal(board):
            return utility(board)

        v = float('inf')
        best_move = None

        for action in actions(board):
            max_result = max_value(result(board, action, 'O'))
            if max_result < v:
                v = max_result
                best_move = action

        return best_move

    if terminal(board):
        return None

    if current_player(board) == 'X':
        return max_value(board)
    else:
        return min_value(board)