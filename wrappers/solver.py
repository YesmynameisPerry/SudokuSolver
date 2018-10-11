__all__ = ["simpleSolve"]

from helpers.minimizer import *
from copy import deepcopy

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