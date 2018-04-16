import json     # for taking json input.

def isattack(board,r,c):
    for i in range(r):      #checks the column c for all rows r present
        if(board[i][c]==1):
            return True
    
    i=r-1
    j=c-1
    while((i>=0) and (j>=0)):       #checks upper left diagonal
        if(board[i][j]==1):
            return True
        i=i-1
        j=j-1
    
    i=r-1
    j=c+1
    while((i>=0) and (j<8)):    # checks upper right diagonal
        if(board[i][j]==1):
            return True
        i=i-1
        j=j+1
    return False
    
def solve(board,row):
    i=0
    while(i<8):
        if(not isattack(board, row, i)):
            board[row][i]=1
            if(row==7):     # checks all 8 row are completed or not
                return True
            else:
                if(solve(board, row+1)):         #if board is partially filled then row=row+1
                    return True
                else:
                    board[row][i]=0     #backtracking and reseting board=0
                    
        i=i+1
    
    if(i==8):
       return False
    
def printboard(board):
    for i in range(8):
        for j in range(8):
            print (str(board[i][j])+"  ",end='')
        print ("\n")
        
board = [[0 for x in range(8)] for x in range(8)]   #8 by 8 zero matrix

if __name__ == '__main__':  #main function started.
    data=[]
    with open('input.json') as f:
        data=json.load(f)   # loads will load the file as string. but load will load the file as it is 
    
    if(data["start"]<0 or data["start"]>7):
        print ("Invalid JSON input")
        exit()
    
    board[0][data["start"]]=1   #Always fixing the queen in first row only
    if(solve(board, 1)):
        print ("Queens problem solved!!!")
        print ("Board Configuration:")
        printboard(board)
    else:  #dead block of code
        print ("Queens problem not solved!!!")
