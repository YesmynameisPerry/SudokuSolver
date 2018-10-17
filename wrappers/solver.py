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
    undecidedCells = [(board[rowIndex][cellIndex], rowIndex, cellIndex) for rowIndex in range(len(board)) for cellIndex in range(len(board[rowIndex])) if type(board[rowIndex][cellIndex]) == list]
    for cell in undecidedCells:
        for valueIndex in range(len(cell[0])):
            possibleValue = cell[0][valueIndex]
            tempBoard = deepcopy(board)
            tempBoard[cell[1]][cell[2]] = possibleValue
            tempBoard = complexSolve(tempBoard)
            if validateBoard(tempBoard): return tempBoard
    return board