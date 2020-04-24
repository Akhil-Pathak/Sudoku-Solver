
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [3,8,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2]
]




def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------|-------|------")
        for  j in range(len(board[0])):
            if j % 3 == 0 and j != 0 :
                print("|" , end = " ")

            if j == 8 :
                print(board[i][j])    

            else:
                print(str(board[i][j]) , end = " ")     


def emptycells_finder(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 :
                return(i,j)

    return False            



def checker(number , positonofemptycell , board):
    for i in range(len(board[0])):
        if board[positonofemptycell[0]][i] == number and positonofemptycell[1] != i: 
            return False

    for j in range(len(board)):
        if board[j][positonofemptycell[1]] == number and positonofemptycell[0] != j:
            return False  

    box_x = positonofemptycell[1] // 3
    box_y = positonofemptycell[0] // 3    

    for i in range(box_y*3 , box_y*3 + 3):
        for j in range(box_x*3 , box_x*3+3):
            if board[i][j] == number and (i,j) != positonofemptycell :
                return False 
    return True


def solver(board):
    emptycells = emptycells_finder(board)
    if not emptycells :
        return True
    else :
        row , col = emptycells  

    for i in range(1,10):
        if checker(i , (row,col) , board):
            board[row][col] = i 
            if solver(board):
                return True
            board[row][col] = 0  
    return False        
  

            
print_board(board)
solver(board)
print("\n" , end = "")
print("//------------------------------------------------//")
print("\n" , end = "")
print_board(board)
print("Finished")
##print("This is bq")
