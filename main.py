# -*- coding: utf-8 -*-
"""
sudoku solver logic

eliminate all numbers that it cannot be

if only one choice in cell:
    choose
    eliminate all numbers that it cannot be

if number only once in row/col/square
    choose
    eliminate all numbers that it cannot be
"""

from helpers.boardMaker import *
from helpers.minimizer import *
from helpers.printer import *
from copy import deepcopy

board = makeBoardFromCsv("board.csv")

printBoard(board)

board = minimize(board)

while True:
    oldBoard = deepcopy(board)
    board = squash(board)
    board = minimize(board)
    if board == oldBoard:
        break

printBoard(board)

