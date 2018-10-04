__all__ = ["makeBoardFromCsv"]

def _allPossibilities():
    return ["1","2","3","4","5","6","7","8","9"]

def _row(line):
    list = line.strip().split(",")[:9]
    for i in range(len(list)):
        if not list[i]:
            list[i] = _allPossibilities()
        else: list[i] = str(list[i])
    return list

# takes a filename for a csv file, spits out a board nested list
def makeBoardFromCsv(filename):
    board = open(filename).readlines()[:9]

    for i in range(len(board)):
        board[i] = _row(board[i])

    return board