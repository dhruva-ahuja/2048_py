from random import randrange
import numpy as np

import helper
import gameplay

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'exit'
BLANK = 0
BLANK_REPR = '_'


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


def play(A, m, n):
    while generateRandom(A, m, n):
        helper.printGrid(A, m, n)
        move = input()
        while not gameplay.playsucessfulmove(A, m, n, move):
            helper.printGrid(A, m, n)
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
    play(grid, N, N)

if __name__ == '__main__':
    main()
