import numpy as np

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'exit'
BLANK = 0
BLANK_REPR = '_'


def moveblanksforward(row, n):
    moved = False
    # move all blanks forward
    writeIndex = n-1
    for i in range(n):
        if row[n-1-i] != BLANK:
            if writeIndex != n-1-i:
                moved = True
            row[writeIndex] = row[n-1-i]
            writeIndex -= 1
    for i in range(writeIndex+1):
        row[i] = BLANK
    return moved


def rightshift(row, n):
    legalmove = False
    legalmove |= moveblanksforward(row, n)
    #operate
    i = n-1
    while i > 0:
        if row[i] == BLANK:
            row[i] = row[i-1]
            row[i-1] = BLANK
        elif row[i] == row[i-1]:
            row[i] = 2*row[i-1]
            row[i-1] = BLANK
        legalmove |= moveblanksforward(row, n)
        i -= 1
    return legalmove


def playsucessfulmove(A, m, n, move):
    legalmove = False
    if move == UP:
        A = np.transpose(np.flip(A, axis=0))
        for i in range(n):
            legalmove |= rightshift(A[i], m)
        A = np.flip(np.transpose(A), axis=0)
    elif move == DOWN:
        A = np.transpose(A)
        for i in range(n):
            legalmove |= rightshift(A[i], m)
        A = np.transpose(A)
        print()
    elif move == RIGHT:
        for i in range(m):
            legalmove |= rightshift(A[i], n)
        print()
    elif move == LEFT:
        A = np.flip(A, axis=1)
        for i in range(m):
            legalmove |= rightshift(A[i], n)
        A = np.flip(A, axis=1)
        print()
    elif move == EXIT:
        quit()
    else:
        print('Illegal move!')
    return legalmove
