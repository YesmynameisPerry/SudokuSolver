from helpers.printer import printError
from helpers.sectionHelper import getFunctions

__all__ = ["validateBoard"]

def validateBoard(board):
    return _isFull(board) and _isSolved(board)

def _isFull(board):
    for row in board:
        for cell in row:
            if type(cell) != str:
                return False
    return True

def _isSolved(board):
    for getFunction in getFunctions:
        for i in range(9):
            if not _containsAllValues(getFunction(i, board)):
                return False
    return True

def _containsAllValues(listOfNine):
    allValues = ["1","2","3","4","5","6","7","8","9"]
    for value in allValues:
        if value not in listOfNine:
            return False
    if len(listOfNine) != 9:
        printError("SOMETHING ISN'T 9 ITEMS LONG")
        return False
    return True
