board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printboard(board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': 
                printboard(board)               
                print(turn + " won.")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printboard(board)               
                print(turn + " won.")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': 
                printboard(board)                
                print(turn + " won.")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': 
                printboard(board)              
                print(turn + " won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': 
                printboard(board)                
                print(turn + " won.")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': 
                printboard(board)                
                print(turn + " won.")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': 
                printboard(board)               
                print(turn + " won.")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printboard(board)               
                print(turn + " won.")
                break 

    
        if count == 9:               
            print("Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            board[key] = " "

        game()

if __name__ == "__main__":
    game()