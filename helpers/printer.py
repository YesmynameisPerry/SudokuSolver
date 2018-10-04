from traceback import print_stack
from time import sleep
from copy import deepcopy

__all__ = ["printBoard", "printRow"]

top = " "+("___ "*3+" ")*3
mid = ("|ˍˍˍ"*3+"|")*3
bot = ("|___"*3+"|")*3
lef = "| "
cen = " | "
big = " || "
rig = " |"

def printError(msg):
    printDelay = 0.2
    print("\033[91m"+msg+"\033[0m\nStack Trace:")
    sleep(printDelay)
    print_stack()
    sleep(printDelay)

def printBoard(board):
    board = deepcopy(board)
    print(top)
    for row in range(len(board)):
        printRow(board[row])
        print(bot if row % 3 == 2 else mid)

def _prettify(listOfNine):
    listOfNine = deepcopy(listOfNine)
    if len(listOfNine) != 9:
        raise Exception("List: ["+", ".join(listOfNine)+"] of length " + str(len(listOfNine)) + " is not 9 elements long")
    for cell in range(len(listOfNine)):
        if type(listOfNine[cell]) == list and len(listOfNine[cell]) > 1:
            listOfNine[cell] = " "
        if type(listOfNine[cell]) == list and len(listOfNine[cell]) == 1:
            listOfNine[cell] = str(listOfNine[cell][0])
            printError("You're prettifying things in helpers.printer._prettify without squishing")
        else:
            listOfNine[cell] = str(listOfNine[cell])
    return listOfNine

def printRow(row):
    row = _prettify(deepcopy(row))
    print(lef + cen.join(row[:3]) + big + cen.join(row[3:6]) + big + cen.join(row[6:]) + rig)