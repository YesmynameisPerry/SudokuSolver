from copy import deepcopy
from helpers.sectionHelper import *

__all__ = ["minimize", "squash", "squish"]

# takes a board, sets all final values to final position
def minimize(board):
    for row in range(9):
        for cell in range(9):
            if type(board[row][cell]) == list and len(board[row][cell]) == 1:
                board[row][cell] = board[row][cell][0]
    return board

def _squishSegment(board, functions, segment):
    listOfCells = functions[0](segment, board)
    for cell in range(9):
        if type(listOfCells[cell] == list):
            for possibility in listOfCells[cell]:
                listOfOthers = [item for sublist in [listOfCells[n] for n in range(9) if n != cell] for item in sublist]
                if possibility not in listOfOthers:
                    listOfCells[cell] = possibility
    return functions[1](segment, listOfCells, board)

def _squashSegment(board, getFunction, segment):
    currentSquare = getFunction(segment, board)
    finalizedList = [currentSquare[i] for i in range(9) if type(currentSquare[i]) == str]
    for cell in range(9):
        if type(currentSquare[cell]) == list:
            currentSquare[cell][:] = [item for item in currentSquare[cell] if item not in finalizedList]
    return board

# takes a board, eliminates all numbers that have been finalised in conflicting spaces
def squash(board):
    board = deepcopy(board)
    for segment in range(9):
        for getFunction in getFunctions:
            board = _squashSegment(board, getFunction, segment)
    return board

# takes a board, for each cell sets a value if it only appears as a possibility once in a row/column/square
def squish(board):
    for segment in range(9):
        for i in range(3):
            board = _squishSegment(board, (getFunctions[i], putFunctions[i]), segment)
    return board