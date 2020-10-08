import sys
import os
import random 
import time

list2 =["A3","A2","A1","B3","B1","B2","C3","C1","C2"]
player1= "X"
player2= "0"
computer0= "0"
computerx= "X"


lista_miscari_random = ["00","01","02","10","11","12","10","11","12"]
allastmovex = "X"
allastmove0 = "0"

def init_board():
    board = [['.','.','.'],
             ['.','.','.'],
             ['.','.','.']]
    return board
board = init_board()

def get_move_ai_lastmove(board,allastmovex):
    
    list_coord= []
    
    list1 = [board[0][0],board[0][1],board[0][2]]
    list9 = [board[1][0],board[1][1],board[1][2]]
    list3 = [board[2][0],board[2][1],board[2][2]]
    list4 = [board[0][0],board[1][1],board[2][2]]
    list5 = [board[0][0],board[1][0],board[2][0]]
    list6 = [board[0][1],board[1][1],board[2][1]]
    list7 = [board[0][2],board[1][2],board[2][2]]
    list8 = [board[0][2],board[1][1],board[2][0]]
    if list1.count(allastmovex) == 2 and list1.count('.') == 1:
        z= 0
        list_coord = []
        for i,x in enumerate(list1):
            
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    
    elif list9.count(allastmovex) == 2 and list9.count('.') == 1:
        z= 1
        list_coord = []
        for i,x in enumerate(list9):
            
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list3.count(allastmovex) == 2 and list3.count('.') == 1:
        z= 2
        list_coord = []
        for i,x in enumerate(list3):
            
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list4.count(allastmovex) == 2 and list4.count('.') == 1:
        z= -1
        list_coord = []
        for i,x in enumerate(list4):
            z= z+1
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list5.count(allastmovex) == 2 and list5.count('.') == 1:
        z= 0
        list_coord = []
        for i,x in enumerate(list5):
           
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list6.count(allastmovex) == 2 and list6.count('.') == 1:
        z= -1
        list_coord = []
        for i,x in enumerate(list6):
            z= z+1
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list7.count(allastmovex) == 2 and list7.count('.') == 1:
        z= -1
        list_coord = []
        for i,x in enumerate(list7):
            z=z+1
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    elif list8.count(allastmovex) == 2 and list8.count('.') == 1:
        z= -1
        list_coord = []
        for i,x in enumerate(list8):
            z=z+1
            if x ==".":
                list_coord.append(z)
                list_coord.append(i)
            else:
                pass
    else:
        board = init_board()
        game = True
        while game:
            
            move = random.choice(lista_miscari_random)
            board = init_board()
            for i in move:
                list_coord.append(int(i))
            x= list_coord[0]
            y = list_coord[1]
            if board[x][y] == ".":
                game = False
            
        else:
            board = init_board()
            move = []

    return tuple(list_coord)

def get_move(board,player1):
    
    list_coord= []
    
    keep_asking = True
    
    while(keep_asking == True):
        move = input(f"please player {player1} moove coord: ").upper()
        if(move=="quit" or move== "QUIT"):
            break
        while (move not in list2):
            move = input("please select corect coord: ").upper()
            if(move=="quit" or move== "QUIT"):
                break
        else:
            list_coord= []
            for x in move:
                
                if(x=="a" or x== "A"):
                    x = 0
                    list_coord.append(x)
                    
                elif(x=="b" or x=="B"):
                    x =1 
                    list_coord.append(x)
                elif (x=="c" or x =="C"):
                    x=2
                    list_coord.append(x)
                else:
                    list_coord.append(int(x)-1)
            
        
        
        if(board[list_coord[0]][list_coord[1]]=='.'):
            keep_asking = False
        else:
            move =""
            
    return tuple(list_coord)

def get_move_ai(board,computer0):
        
    list_coord= []
    
    keep_asking = True
    
    while(keep_asking == True):
        move = random.choice(list2)
        list_coord= []
        for x in move:
            
            if(x== "A"):
                x = 0
                list_coord.append(x)
                
            elif(x=="B"):
                x =1 
                list_coord.append(x)
            elif (x =="C"):
                x=2
                list_coord.append(x)
            else:
                list_coord.append(int(x)-1)
            
        
        
        if(board[list_coord[0]][list_coord[1]]=='.'):
            keep_asking = False
        else:
            move =""
    return tuple(list_coord)

def mark(board,player1,row,col):
    
    board[row][col]= player1
        
    return board
    




def has_won(board, player1):
    if board[0][0]==player1 and board[0][1] ==player1 and board[0][2] == player1:
        return False
    elif board[1][0]==player1 and board[1][1] ==player1 and board[1][2] == player1:
        return False
    elif board[2][0]==player1 and board[2][1] ==player1 and board[2][2] == player1:
        return False
    elif board[0][0]==player1 and board[1][1] ==player1 and board[2][2] == player1:
        return False
    elif board[0][0]==player1 and board[1][0] ==player1 and board[2][0] == player1:
        return False
    elif board[0][1]==player1 and board[1][1] ==player1 and board[2][1] == player1:
        return False
    elif board[0][2]==player1 and board[1][2] ==player1 and board[2][2] == player1:
        return False
    elif board[0][2]==player1 and board[1][1] ==player1 and board[2][0] == player1:
        return False
    else:
        return True

def is_full(board):
    
    if "." in board[0] or "." in board[1] or "." in board[2]:       
        return False
    else:
        return True

def print_board(board):
    print("   1  "+ "   2  "+"    3  ")
    print("A  " +f"{board[0][0]} "+ " |  "+f"{board[0][1]}"+ "  |   "+f"{board[0][2]}")
    print("------+-----+------")
    print("B  " +f"{board[1][0]} "+ " |  "+f"{board[1][1]}"+ "  |   "+f"{board[1][2]}")
    print("------+-----+------")
    print("C  " +f"{board[2][0]} "+ " |  "+f"{board[2][1]}"+ "  |   "+f"{board[2][2]}")



def print_result(board):
    
    
    if(has_won(board,player1)== False):
        
        print(f"player {player1} has won !")
        return False
    elif(has_won(board,player2)==False):
        
        print(f"player {player2} has won !")
        return False
    elif(has_won(board,computerx)==False):
        
        print(f"player {computerx} has won !")
        return False
    elif(has_won(board,computer0)==False):
        
        print(f"player {computer0} has won !")
        return False
    elif(has_won(board,allastmovex)==False):
        
        print(f"player {allastmovex} has won !")
        return False
    elif(has_won(board,allastmove0)==False):
        
        print(f"player {allastmove0} has won !")
        return False
    elif is_full(board) == True:
        print("This is a Tie")
        return False
    else: 
        return True




def tic_toe(x):
    
    if(x==1):
        board =init_board()
        i = 0
        while i<15:
            print_board(board)
            coord =get_move(board,player1)
            row = coord[0]
            col = coord[1]
            mark(board,computerx,row,col)
            i= i+1
            if(print_result(board)==False):
                print_board(board)
                break
            
            print_board(board)
            coord =get_move(board,player2)
            row = coord[0]
            col = coord[1]
            mark(board,computer0,row,col)
            i=i+1
            if(print_result(board)==False):
                print_board(board)
                break
    elif x ==2:
        board =init_board()
        i = 0
        while i<15:
            print_board(board)
            coord =get_move(board,player1)
            row = coord[0]
            col = coord[1]
            mark(board,computerx,row,col)
            i= i+1
            time.sleep(2)
            if(print_result(board)==False):
                print_board(board)
                break
            
            print_board(board)
            coord =get_move_ai(board,computer0)
            row = coord[0]
            col = coord[1]
            mark(board,computer0,row,col)
            i=i+1
            if(print_result(board)==False):
                print_board(board)
                break
    elif x ==3:
        board =init_board()
        
        i = 0
        while i<15:
            print_board(board)
            coord =get_move_ai(board,computerx)
            row = coord[0]
            col = coord[1]
            mark(board,computerx,row,col)
            i= i+1
            if(print_result(board)==False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord =get_move(board,player2)
            row = coord[0]
            col = coord[1]
            mark(board,computer0,row,col)
            i=i+1
            time.sleep(2)
            if(print_result(board)==False):
                print_board(board)
                break

                
    elif x ==4:
        board =init_board()
        
        i = 0
        while i<15:
            print_board(board)
            coord =get_move_ai(board,computerx)
            row = coord[0]
            col = coord[1]
            mark(board,computerx,row,col)
            i= i+1
            if(print_result(board)==False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord =get_move_ai(board,computer0)
            row = coord[0]
            col = coord[1]
            mark(board,computer0,row,col)
            i=i+1
            time.sleep(2)
            if(print_result(board)==False):
                print_board(board)
                break
    elif x == 5:
        board =init_board()
        
        i = 0
        while i<15:
            print_board(board)
            coord =get_move(board,player1)
            row = coord[0]
            col = coord[1]
            mark(board,player1,row,col)
            i= i+1
            if(print_result(board)==False):
                print_board(board)
                break

            time.sleep(1)
            print_board(board)
            coord =get_move_ai_lastmove(board,allastmovex)
            row = coord[0]
            col = coord[1]
            mark(board,allastmove0,row,col)
            i=i+1
            time.sleep(1)
            if(print_result(board)==False):
                print_board(board)
                break         
    elif x ==6:
        board =init_board()
        
        i = 0
        while i<15:
            print_board(board)
            coord =get_move_ai_lastmove(board,allastmove0)
            row = coord[0]
            col = coord[1]
            mark(board,computerx,row,col)
            i= i+1
            if(print_result(board)==False):
                print_board(board)
                break

            time.sleep(2)
            print_board(board)
            coord =get_move(board,player2)
            row = coord[0]
            col = coord[1]
            mark(board,player2,row,col)
            i=i+1
            time.sleep(2)
            if(print_result(board)==False):
                print_board(board)
                break      
def main_menu():
    print("Game Mode :\n","1. Player   Vs Player \n",'2. Player   Vs Al Bundy \n',"3. Al Bundy(easy) Vs Player \n","4. Al Bundy Vs Al Bundy \n", 
    "5. Player vs Safe Al Bundy \n", "6. Al Bundy Safe vs Player ")
    x= int(input("Select 1 , 2 , 3 , 4 ,5 or 6 : "))
    tic_toe(x)


if __name__ == '__main__':
    main_menu()             

    











        


    

