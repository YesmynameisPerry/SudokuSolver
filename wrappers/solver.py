__all__ = ["simpleSolve", "complexSolve"]

from helpers.minimizer import *
from copy import deepcopy
from helpers.validator import *

def simpleSolve(board):
    board = deepcopy(board)
    board = minimize(board)
    while True:
        oldBoard = deepcopy(board)
        board = squash(board)
        board = minimize(board)
        board = squish(board)
        if board == oldBoard: break
    return board

def complexSolve(board):
    board = simpleSolve(board)
    if validateBoard(board): return board
    undecidedCells = [board[rowIndex][cellIndex] for rowIndex in range(board) for cellIndex in range(len(board[rowIndex])) if type(cell) == list]
    print("Undecided Cells", undecidedCells)
    undecidedCells[0] = "3"
    return board