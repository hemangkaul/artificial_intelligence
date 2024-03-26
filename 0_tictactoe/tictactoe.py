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
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for spot in row:
            if spot is not EMPTY:
                count += 1
    if count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY or i < 0 or j < 0:
        raise Exception("Invalid move")
    else:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] and row[1] == row[2]:
            return row[0]

    if board[0][0] is not EMPTY and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] is not EMPTY and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] is not EMPTY and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    if board[0][0] is not EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not X and winner(board) is not O:
        for row in board:
            for spot in row:
                if spot == EMPTY:
                    return False
        return True
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move_list = []
    if terminal(board):
        return None
    elif player(board) == X:
        best_value = float('-inf')
        best_move = None
        moves = actions(board)
        for move in moves:
            value = minimax_helper(result(board, move))
            if value > best_value:
                best_value = value
                best_move = move
                if value == 1:
                    break
    elif player(board) == O:
        best_value = float('inf')
        best_move = None
        moves = actions(board)
        for move in moves:
            value = minimax_helper(result(board, move))
            if value < best_value:
                best_value = value
                best_move = move
                if value == - 1:
                    break
    return best_move


def minimax_helper(board):
    move_list = []
    if terminal(board):
        return utility(board)
    else:
        moves = actions(board)
        for move in moves:
            move_list.append(minimax_helper(result(board, move)))
        if player(board) == X:
            return max(move_list)
        elif player(board) == O:
            return min(move_list)
