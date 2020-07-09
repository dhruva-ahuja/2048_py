from random import randrange

UP = 'w'
DOWN = 's'      
LEFT = 'a'
RIGHT = 'd'
EXIT = 'exit'
BLANK = '_'


def printGrid(A, m, n):
    for i in range(m):
        for j in range(n):
            print(A[i][j], end='|')
        print()

def getEmptySlots(A, m, n):
    empty = []
    for i in range(m):
        for j in range(n):
            if A[i][j] == '_':
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


def playmove(A, m, n, move):
    if move == UP:
        for j in range(m):
            for i in range(n-1,-1,-1):
                if A[i][j] != BLANK and A[i-1][j] == BLANK:
                    A[i-1][j],A[i][j] = A[i][j],BLANK


        print()
        
    elif move == DOWN:
        


        print()
    elif move == RIGHT:
        for i in range(m):
            for j in range(n):
                if A[i][j] == BLANK:
                    A[i].pop(j)
                    A[i].insert(0,BLANK)
            for j in range(n-2,-1,-1):        
                if A[i][j] == A[i][j+1]and A[i][j] != BLANK:
                    A[i][j+1]  =  2*A[i][j+1]
                    A[i][j] = BLANK
            for j in range(n):
                if A[i][j] == BLANK:
                    A[i].pop(j)
                    A[i].insert(0,BLANK)        
                
                   
        # Write something here
        print()
    elif move == LEFT:
        for i in range(m):
            for j in range(n-1,-1,-1):
                if A[i][j] == BLANK:
                    A[i].remove(BLANK)
                    A[i].append(BLANK)
            for j in range(1,n):
                if A[i][j] == A[i][j-1]and A[i][j] != BLANK:
                    A[i][j-1]  =  2*A[i][j]
                    A[i][j] = BLANK
            for j in range(n-1,-1,-1):
                if A[i][j] == BLANK:
                    A[i].remove(BLANK)
                    A[i].append(BLANK)        
                    
        print()
    elif move == EXIT:
        quit()
    else:
        print('Illegal move!')


def gamePlay(A, m, n):
    while generateRandom(A, m, n):
        printGrid(A, m, n)
        move = input()
        playmove(A, m, n, move)
    

def main():
    print('Welcome to 2048, select the difficulty:')
    print('1. 4X4')
    choice = int(input())
    N = 0
    if choice == 1:
        N = 4
    else:
        print('Invalid input')
    
    grid = [['_' for i in range(N)] for i in range(N)]
    gamePlay(grid, N, N)

if __name__ == '__main__':
    main()
print('Game over')