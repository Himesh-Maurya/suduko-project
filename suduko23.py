

def findEmptyPosition(grid,emptyPosition,n):
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 0):
                emptyPosition[0] = i
                emptyPosition[1] = j
                return True
    return False

def isSafeInRow(grid,row,num,n):
    for i in range(n):
        if(grid[row][i] == num):
            return False
    return True

def isSafeInCol(grid,col,num,n):
    for i in range(n):
        if(grid[i][col] == num):
            return False
    return True

def isSafeInBoard(grid,row,col,num,n):
    rowFactor = row - (row%3)
    colFactor = col - (col%3)
    for i in range(3):
        for j in range(3):
            if(grid[i+rowFactor][j+colFactor] == num):
                return False
    return True            


def isSafe(grid,row,col,i,n):
    if(isSafeInRow(grid,row,i,n) and isSafeInCol(grid,col,i,n) and isSafeInBoard(grid,row,col,i,n)):
        return True
    return False    
    
def solveSudoku(grid,n):
    '''
    emptyPosition is a list
    lenght = 2
    0 th position have row number
    1st position have column number
    '''
    emptyPosition = [-1,-1]
    if(not findEmptyPosition(grid,emptyPosition,n)):
        return True
    row = emptyPosition[0]
    col = emptyPosition[1]
    for i in range(1,10):
        if(isSafe(grid,row,col,i,n)):
            grid[row][col] = i
            if(solveSudoku(grid,n)):
                return True
            grid[row][col] = 0
    return False




def solver23(grid):
    if(solveSudoku(grid,9)):
        return grid
    else:
        return "no"
        
