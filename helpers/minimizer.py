from copy import deepcopy
from helpers.sectionHelper import *

__all__ = ["minimize", "squash"]

from helpers.sectionHelper import getSquare, getRow, getColumn

# takes a board, sets all final values to final position
def minimize(board):
    for row in range(9):
        for cell in range(9):
            if type(board[row][cell]) == list and len(board[row][cell]) == 1:
                board[row][cell] = board[row][cell][0]
    return board

# takes a board, eliminates all numbers that have been finalised in conflicting spaces
def squash(board):
    board = deepcopy(board)
    board = _squashSegment(board, getSquare)
    board = _squashSegment(board, getRow)
    board = _squashSegment(board, getColumn)
    return board

def _squashSegment(board, getFunction):
    for square in range(9):
        currentSquare = getFunction(square, board)
        finalizedList = [currentSquare[i] for i in range(9) if type(currentSquare[i]) == str]
        for cell in range(9):
            if type(currentSquare[cell]) == list:
                currentSquare[cell][:] = [item for item in currentSquare[cell] if item not in finalizedList]
    return board
