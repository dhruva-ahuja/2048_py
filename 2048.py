from random import randrange
import numpy as np

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'exit'
BLANK = 0
BLANK_REPR = '_'

def printGrid(A, m, n):
    for i in range(m):
        for j in range(n):
            symbol = A[i][j]
            if symbol == BLANK:
                symbol = BLANK_REPR
            print(symbol, end='|')
        print()

def getEmptySlots(A, m, n):
    empty = []
    for i in range(m):
        for j in range(n):
            if A[i][j] == BLANK:
                empty.append([i, j])
    return empty

def generateRandom(A, m, n):
    emptySlots = getEmptySlots(A, 4, 4)
    l = len(emptySlots)
    if l == 0:
        return False
    newIndex = randrange(l)
    newNumber = 2**randrange(1, 3)
    A[emptySlots[newIndex][0]][emptySlots[newIndex][1]] = newNumber
    return True

def moveblanksforward(row, n):
    moved = False
    # move all blanks forward
    writeIndex = n-1
    for i in range(n):
        if row[n-1-i] != BLANK:
            row[writeIndex] = row[n-1-i]
            writeIndex -= 1
    for i in range(writeIndex+1):
        row[i] = BLANK
        moved = True
    return moved

def rightshift(row, n):
    legalmove = False
    legalmove |= moveblanksforward(row, n)
    #operate
    i = n-2
    while i >= 0:
        if row[n-i-1] == BLANK:
            row[n-i-1] = row[n-i-2]
            row[n-i-2] = BLANK
            legalmove = True
            i-=2
        elif row[n-i-1] == row[n-i-2]:
            row[n-i-1] = 2*row[n-i-2]
            row[n-i-2] = BLANK
            legalmove = True
            i-=2
        else:
            i-=1
    legalmove |= moveblanksforward(row, n)
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


def gamePlay(A, m, n):
    while generateRandom(A, m, n):
        printGrid(A, m, n)
        move = input()
        while not playsucessfulmove(A, m, n, move):
            printGrid(A, m, n)
            move = input()
    

def main():
    print('Welcome to 2048, select the difficulty:')
    print('1. 4X4')
    choice = int(input())
    N = 0
    if choice == 1:
        N = 4
    else:
        print('Invalid input')
    
    grid = np.array([[BLANK for i in range(N)] for i in range(N)])
    gamePlay(grid, N, N)

if __name__ == '__main__':
    main()
