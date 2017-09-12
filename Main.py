# coding=utf-8


#functional tic tac toe by Julián Gutiérrez Hopper

from IPython.display import clear_output

#Global variables
t = range(1,10)
player1 = 'X'
player2 = 'O'
pl = 1
count = 1
win = False

#Functions
def paint_board (): 
    '''Paints list into 3x3 table'''
    print' ----- '
    print'|'+str(t[0])+'|'+str(t[1])+'|'+str(t[2])+'|'
    print'|'+str(t[3])+'|'+str(t[4])+'|'+str(t[5])+'|'
    print'|'+str(t[6])+'|'+str(t[7])+'|'+str(t[8])+'|'
    print' ----- '
def player_selection (count):
    '''Switches between players. Takes one arg: count'''
    if count%2 == 0:
        pl = 2
    else:
        pl = 1
    return pl
def player_input (pl,t): 
    '''Inputs player selection while checking for errors. Takes pl and t args'''
    while True:
        try:
            move = int(input("Player {}, which is your next move? ".format(pl)))
        except:
            print 'Please input numbers from keypad.\n'
        else:
            if move not in range(1,10):
                print 'Please keep within the range of 1 to 9.\n'
            elif move != t[move-1]:
                print 'Sorry, cell in use. Please pick another.'
            else:
                break    
    return move
def table_update (move,pl,t): 
    '''updates table to reflect game state. takes move, pl and t args'''
    if pl == 1:
        t[move-1] = player1
    else:
        t[move-1] = player2
    
    return t
def win_state (win):            
    '''checks for win state. Takes win bool'''
    if (t[0] == t[1] == t[2]) or (t[3] == t[4] == t[5]) or (t[6] == t[7] == t[8]) or (t[0] == t[3] == t[6]) or (t[1] == t[4] == t[7]) or (t[2] == t[5] == t[8]) or (t[0] == t[4] == t[8]) or (t[2] == t[4] == t[6]):
        win = True
    else:
        win = False   
    return win
def replay ():
    '''asks if players want a replay. Takes no args'''
    if str.lower(raw_input('Would you like to play again? Y/N: ')) == 'y':
        restart()
    else:
        win = True
        print 'kthxbye!'
        return win 
def restart ():
    #restarts the game by resetting gamestate
    global t 
    global win
    global count
    
    t = range(1,10)
    win = False
    count = 1
    return t,win,count
def draw_check(count):
    '''Checks the draw state. Can only be reached after 9 moves'''
    if count == 10:
        print 'DRAW!'
        clear_output()
        replay()

#Main
print "WELCOME TO MY TIC TAC TOE!"
while win != True: 
    draw_check(count)
    paint_board()
    pl = player_selection(count)
    move = player_input(pl,t)
    table_update(move,pl,t)
    if win_state(win):
        print "Congratulations player {}!".format(player_selection(count))
        win = replay()
        clear_output()
    count +=1
    clear_output()
