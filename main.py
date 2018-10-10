# -*- coding: utf-8 -*-
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

