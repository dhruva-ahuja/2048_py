from os import system, name

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'exit'
BLANK = 0
BLANK_REPR = '_'


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def printGrid(A, m, n):
    clear()
    for i in range(m):
        for j in range(n):
            symbol = A[i][j]
            if symbol == BLANK:
                symbol = BLANK_REPR
            print(symbol, end='|')
        print()
