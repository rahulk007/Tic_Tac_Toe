
def display_board(board):


    a=('\n ____ ____ ____ ')
    b=(f'\n| {board[0]}  | {board[1]}  | {board[2]}  |')
    c=(f'\n| {board[3]}  | {board[4]}  | {board[5]}  |')
    d=(f'\n| {board[6]}  | {board[7]}  | {board[8]}  |')
    print(a,b,a,c,a,d,a)


#display_board(test_board)


def player_input():
    player1="wrong"
    player2=''


# while the player choice is not x or y keep asking for a correct choice
    while player1 not in ['X','O']:

        player1=input("Please pick a marker X or O:")

        if player1 not in ['X','O']:
            print('invaild entry!\nPlease select from X or O')
    if player1=='X':
        return ('X','O')
    elif player1=='O':
        return ('O','X')





#player_input()




def place_marker(board,marker,position):
    # update the postion on the board with the given marker at defined position
    board[position]= marker
    return board

# test run for updating the position with marker
#board = ['','X','O','X','O','X','O','X','O']
#position =player_choice()
#place_marker(board,"$",position)
#display_board(board)

def win_check(board,mark):

    won = False

    #checking for winner for the given marker
    #horizontal line check
    if board[0:3]==[mark]*3 or board[3:6]==[mark]*3 or board[6:]==[mark]*3:
         won = True
    #vertical line check
    elif board[0:7:3]==[mark]*3 or board[1:9:3]==[mark]*3 or board[2::3]==[mark]*3:
         won=True
    #diagonal line checking
    elif board[0::4]==[mark]*3 or board[2:7:2]==[mark]*3:
         won=True
    else:
        pass
    return won

#win_check(board,'X')

import random
def choose_first():
    start=''
    x=random.randint(1,2)

    if x==1:
       start=player1
       print('player1 goes first!')
    elif x==2:
       start=player2
       print('palyer2 goes First!')
    return start


#choose_first()

def space_check(board,position):
    space_available= None

    if board[position]=='X' or board[position]=='O':
        space_available=False

    else:
        space_available=True
    return space_available

#x=space_check(board,1)
#print(x)

def full_board_check(board):

    board_full= None
    num_board_count=0

    for i in board:
        if i =='X' or i=='O':
            num_board_count+=1
        else:
            pass
    if num_board_count==9:
        board_full=True
    else:
        board_full=False

    return board_full



#x=full_board_check(board)



def player_choice(board):

    choice='wrong'
    within_range=False


    while choice.isdigit()==False or within_range==False:
        choice=input('enter the board position in from(0-8):')

        if choice.isdigit()==False:
            print('invalid input! enter a number')

        if choice.isdigit()==True:
            if int(choice) in range(0,9):
                within_range=True
            else:
                print('number not in the range(0-8)')
        if space_check(board,int(choice))==False:
            choice='wrong'
            print('position taken, choose another position')
        else:
            pass


    return int(choice)



#position=player_choice(board)
#print(position)



def replay():
    play_again=None

    answer=''

    while answer not in ['Y','N']:
        answer=input('Do want to play again?\nY or N: ')

        if answer in ['Y','N']:
            pass
        else:
            print('choose Y or N')
        if answer=='Y':
            play_again= True
        elif answer=='N':
            play_again=False

    return play_again

#x=replay()
#print(x)


print('Welcome to Tic Tac Toe!')





while True:

     board=['']*10
     player1,player2=player_input()

     turn = choose_first()
     print(turn+'will go first')

     play=input('want to play Y or N')

     if play=='Y':
         game_on=True
     if play=='N':
        game_on=False
     while game_on:
          if turn==player1:
             display_board(board)

             position=player_choice(board)

             place_marker(board,player1,position)



             if win_check(board,player1)==True:
                 display_board(board)
                 print('player 1 has won the game')
                 game_on=False
             else:
                 if full_board_check(board)==True:
                    print('Its a draw')
                    display_board(board)
                    game_on=False

                 else:
                      turn=player2


          else:
             if turn==player2:
                display_board(board)

                position=player_choice(board)

                place_marker(board,player2,position)



                if win_check(board,player2)==True:
                   display_board(board)
                   print('player 2 has won the game')
                   game_on=False
                else:
                    if full_board_check(board)==True:
                      print('Its a draw')
                      display_board(board)
                      game_on=False

                    else:
                        turn=player1
     if not replay():

        break
