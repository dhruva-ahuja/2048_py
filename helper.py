
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
