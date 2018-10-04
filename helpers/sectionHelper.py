__all__ = ["getSquare", "getRow", "getColumn", "putSquare", "putColumn", "putRow"]

from math import floor

# get functions return a section of the board as a copy
def getSquare(pos, board):
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    index = pos
    return [
        board[3*floor(index/3)][3*(index % 3)],
        board[3*floor(index/3)][1+3*(index % 3)],
        board[3*floor(index/3)][2+3*(index % 3)],
        board[3*floor(index/3)+1][3*(index % 3)],
        board[3*floor(index/3)+1][1+3*(index % 3)],
        board[3*floor(index/3)+1][2+3*(index % 3)],
        board[3*floor(index/3)+2][3*(index % 3)],
        board[3*floor(index/3)+2][1+3*(index % 3)],
        board[3*floor(index/3)+2][2+3*(index % 3)]
    ]

def getRow(pos, board):
    pos = int(pos)
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    return [board[pos][n] for n in acceptedValues]

def getColumn(pos, board):
    pos = int(pos)
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    return [board[n][pos] for n in acceptedValues]

# put functions overwrite the board at the position with the input
def putSquare(pos, square, board):
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    index = acceptedValues.index(pos)
    board[3*floor(index/3)][3*(index % 3)] = square[0]
    board[3*floor(index/3)][1+3*(index % 3)] = square[1]
    board[3*floor(index/3)][2+3*(index % 3)] = square[2]
    board[3*floor(index/3)+1][3*(index % 3)] = square[3]
    board[3*floor(index/3)+1][1+3*(index % 3)] = square[4]
    board[3*floor(index/3)+1][2+3*(index % 3)] = square[5]
    board[3*floor(index/3)+2][3*(index % 3)] = square[6]
    board[3*floor(index/3)+2][1+3*(index % 3)] = square[7]
    board[3*floor(index/3)+2][2+3*(index % 3)] = square[8]
    return board

def putRow(pos, row, board):
    pos = int(pos)
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    board[pos] = row
    return board

def putColumn(pos, column, board):
    pos = int(pos)
    acceptedValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if not pos in acceptedValues:
        raise SyntaxError("pos: "+str(pos)+" not in accepted list: [" + ", ".join(acceptedValues)+"]")
    for n in acceptedValues:
        board[n][pos] = column[n]
    return board
