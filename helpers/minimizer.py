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

# takes a board, for each cell sets a value if it only appears as a possibility once in a row/column/square
def squish(board):
    count = 0
    gets = [(getSquare, putSquare), (getColumn, putColumn), (getRow, putRow)]
    for i in range(9):
        for boardFunction in gets:
            listOfCells = boardFunction[0](i, board)
            for cell in range(9):
                if type(listOfCells[cell] == list):
                    for possibility in listOfCells[cell]:
                        listOfOthers = [item for sublist in [listOfCells[n] for n in range(9) if n != cell] for item in sublist]
                        if possibility not in listOfOthers:
                            count += 1
                            listOfCells[cell] = possibility
            board = boardFunction[1](i, listOfCells, board)
    return board