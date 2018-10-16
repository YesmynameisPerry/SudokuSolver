# -*- coding: utf-8 -*-
from helpers.boardMaker import *
from wrappers.printer import *
from wrappers.solver import *
from helpers.validator import *

board = makeBoardFromCsv("board.csv")

printBoard(board)


board = complexSolve(board)

printBoard(board)
print("Board solved:", validateBoard(board))
