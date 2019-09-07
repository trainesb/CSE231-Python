    ###########################################################
    #  Computer Project #11
    #
    #   GoPiece(object):
    #   
    #   def __init__: initialiezes the color of the piece and sets the
    #   default to black. if the color is not 'black' or 'white' then MyError
    #   is raised.   
    #   
    #   def __str__: prints the correct piece repsective to the color
    #   then prints the color as a string.
    #
    #   def get_color: returns the color of the piece as a string
    #
    #   Gomoku(object):
    #
    #   def __init__: initializes the game board. The default size is 15x15
    #   with a win_count of fice, starting with player 'black'.  
    #
    #   assign_piece: assign a piece to the board or raise and Error. 
    #
    #   get_current_player: returns the current player as a string
    #
    #   switch_current_player: switch players
    #
    #   def current_player_is_winner: test to see if a player has won. They won
    #   if they have fice pieces in a row horizontally, vertically, or 
    #   diagnolly.
    #
    ###########################################################

class GoPiece(object):
    ''' sets the pieces color or returns an error, prints the correct piece
    respective to its color, and prints the color name as a string.'''
    def __init__(self,color= 'black'):
        '''set the default color to black, if color not black or white raise
        error, and set color to private.'''
        if color == "black":
            self.__color = color
        elif color == "white":
            self.__color = color
        else:
            raise MyError('Wrong color.')
    
    def __str__(self):
        '''prints the correct dot respective to its color'''
        if self.__color == 'black':
            return ' ● '
        else:
            return ' ○ '

    def get_color(self):
        ''' prints tehe color of the piece as a string'''
        return str(self.__color)
    
    def __repr__(self):
        return self.__str__()

#a = GoPiece('white') 
#print("__str__",a)
#print("get_color",a.get_color())
           
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''init sets up the game board and current_player. will assign a peace or
    raise an error. will return the current player as a string, switch player, 
    or tell if a player has won.'''
    def __init__(self,board_size=15,win_count=5,current_player='black'):
        '''sets board_size to 15, win_count to 5, and color to 'black' by 
        default. if color is not 'black' or 'white' Error is raised.'''
        self.__board_size = int(board_size)
        self.__win_count = int(win_count)
        if current_player == "black":
            self.__current_player = current_player
        elif current_player == "white":
            self.__current_player = current_player
        else:
            raise MyError('Wrong color.')
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for \
                           i in range(self.__board_size)]
 
            
    def assign_piece(self,piece,row,col):
        '''assigns a piece to the board according to row and col. If the spot
        is taken or the row and col are out of range a Error is raised.'''
        row = int(row)-1
        col = int(col)-1
        if (0<=row<=self.__board_size) != True: 
            raise MyError('Invalid position.')
        elif (0<=col<=self.__board_size) != True:
            raise MyError('Invalid position.')
        elif self.__go_board[row][col] != ' - ':
            raise MyError('Position is occupied.')
        else:
            self.__go_board[row][col]=piece
                      
            
    def get_current_player(self):
        '''Returns the current player as a string'''
        return self.__current_player
    
    def switch_current_player(self):
        """Switch player."""
        if self.__current_player == "black":
            self.__current_player = 'white'
        else:
            self.__current_player = "black"
        return self.__current_player
        
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' \
                                   else '○')
        return s
    
    def __repr__(self):
        return self.__str__()
        
    def current_player_is_winner(self):
        ''' Checks the game board vertically and horizontally to see if the 
        current player has won.'''
        #horizontal
        for rows in self.__go_board:
            r = 0
            for a in rows:
                if a == ' - ':
                    if r == self.__win_count:
                        return True
                    else:
                        r = 0
                elif self.get_current_player() == 'white':
                    if a.get_color() == 'white':
                        r += 1
                        if r == self.__win_count:
                            return True
                    else:
                        r = 0
                else:
                    if a.get_color() == 'black':
                        r += 1
                        if r == self.__win_count:
                            return True
                    else:
                        r = 0

        #vertical
        col=0
        for i in range(self.__board_size):
            for rows in self.__go_board:
                if rows[i] == ' - ':
                    if col == self.__win_count:
                        return True
                    else:
                        col = 0
                elif self.get_current_player() == 'white':
                    if rows[i].get_color() == 'white':
                        col += 1
                        if col == self.__win_count:
                            return True
                    else:
                        col = 0
                else:
                    if rows[i].get_color() == 'black':
                        col += 1
                        if col == self.__win_count:
                            return True
                    else:
                        col = 0
        
        #diagnol down
        start = (self.__board_size)-(self.__win_count)
        while start > -1:
            for i in range(self.__board_size):
                try:
                    row = self.__go_board
                    list = [row[start][i],row[start+1][i+1],row[start+2][i+2],\
                            row[start+3][i+3],row[start+4][i+4]]
                    if ' - ' in list:
                        continue
                    else:
                        if len(list) == self.__win_count:
                            return True
                except IndexError:
                    continue
            start -= 1

        
        #diagnol up
        w = (self.__board_size)-(self.__win_count)-1
        x = (self.__board_size)-1
        while x > -1:
            for start in range(w,-1,-1):
                try:
                    row = self.__go_board
                    list = [row[x][start],row[x-1][start+1],row[x-2][start+2],\
                            row[x-3][start+3],row[x-4][start+4]]
                    if ' - ' in list:
                        continue
                    else:
                        if len(list) == self.__win_count:
                            return True
                except IndexError:
                    break
            x -= 1
        
        return False
            

#b = Gomoku( '15','5','black')
#print()
#b.assign_piece(' ● ',9,1)
#b.assign_piece(' ● ',2,1)
#b.assign_piece(' ● ',3,1)
#b.assign_piece(' ● ',4,1)
#b.assign_piece(' ● ',5,1)
#print()
#print("__str__",b)

#print()
#b.current_player_is_winner()
        
def main():

    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        try:
            while len(play_list) != 2:
                raise MyError("Incorrect input.")
                play = input("Input a row then column separated by a comma (q to quit): ")
                
            for i in play_list:
                if i.isalpha() == True:
                    raise MyError("Incorrect input.")
            
            current_player = board.get_current_player()
            piece = GoPiece(current_player)
            board.assign_piece(piece, play_list[0],play_list[1])
            if board.current_player_is_winner() == True:
                print(board)
                print("{} Wins!".format(board.get_current_player()))
                break
            else:
                board.switch_current_player()
                                     


        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()



