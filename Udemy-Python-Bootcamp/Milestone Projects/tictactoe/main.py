# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

p1 = raw_input("Pick a letter:   ")
p2 = raw_input("Pick other letter:   ")

board = [['','',''],['','',''],['','','']]


def check(board):
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Write a function that takes in the board and a player marker and checks it theres a win or a tie.
# The checking for a win should be a series of a bunch checks, for example: (board[7] == board[8] == board[9] == marker)would check the first top row if they all match a player's marker.
# Check for a tie (this means nobody won and the board list is full
    for i in board:
        if (i[0] == i[1] == i[2]) and i[0] != '':
            print i[0] + " is the winner!"
            return True
        return 0



def game():

    player = p1
    print "Starts player %s"%player


    for i in range(0,10):

        print "Player %s turn"%player

        row = raw_input("Pick a row: ")
        col = raw_input("Pick a column: ")

        board[int(row)-1][int(col)-1] = player

        plan = " ______________" + "\n" + "|" + "  " + str(board[0][0]) + "  " + "|" + "  " + str(board[0][1]) + "  " + "|" + "  " + str(board[0][2]) + "  " +"|" + "\n" + " ______________" + "\n"               + "|" + "  " + str(board[1][0]) + "  " + "|" + "  " + str(board[1][1]) + "  " + "|" + "  " + str(board[1][2]) + "  " + "|" + "\n" + " ______________" + "\n" + "|" + "  " + str(board[2][0]) + "  " + "|" + "  " \
               + str(board[2][1]) + "  " + "|" + "  " + str(board[2][2]) + "  " + "|" + '\n'

        if player == p1:
            player = p2
        else:
            player = p1

        print plan
        check(board)

        if check(board)==True:
            replay()




def replay():
    # Ask if players want to play again.
    odp = raw_input("Wanna play again? [Y/N] ")
    if odp == 'Y':
        game()
    else:
        return 0

game()

