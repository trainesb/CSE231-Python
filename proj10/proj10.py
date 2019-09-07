    ###########################################################
    #  Computer Project #10
    #
    #   count_mills(board, player) takes two paramters the board which is
    #   imported, and the player we are counting for. The function then counts
    #   hoe many mills the player has.
    #
    #   place_piece_and_remove_opponents(board, player, destination) takes
    #   three paramters.  The function will place a piece on the board for the 
    #   relavent player and if it can't place the point will return an error.
    #   The function also remove an opponent peace if a new mill is formed
    #
    #   move_piece(board, player, origin, destination) takes four paramters.
    #   THe function calls place_piece_and_remove_opponents() to place a piece
    #   and to see if there were any new mills formed. It also removs the
    #   original
    #
    #   points_not_in_mills(board, player), this function creates a list of
    #   points that the player has. if the player has a mill then another list
    #   is made for those points in the mill. Once all mill points are
    #   collected. THe two lists are changed to a set and a new set is created
    #   with elements that were not in the mill set, which is returned
    #
    #   placed(board,player), this function creates a list with all the points
    #   the player has and returns it.
    #
    #   remove_piece(board, player) thhis function calls the lsit of points
    #   not in a mill and the points placed. If the point that wants to be
    #   removed is not in "points not in mill" and the set length isnt 0 then
    #   error is returned and the user is prompted again. Same if the point is
    #   not valid
    #   
    #   is_winner(board, player), this function takes the list of pieces placed
    #   if the list has  alength less then 3 the player has lost and the bool
    #   is changed to True and returned.
    #
    #   
    #
    ###########################################################


class Board(object):

    #Dictionary containing adjacencies
    ADJACENCY = {"a1": ["d1", "a4"],
        "d1": ["a1", "d2", "g1"], "g1": ["d1", "g4"], "b2": ["b4", "d2"],
        "d2": ["b2", "d1", "d3", "f2"], "f2": ["d2", "f4"],
        "c3": ["c4", "d3"], "d3": ["c3", "d2", "e3"], "e3": ["d3", "e4"],
        "a4": ["a1", "a7", "b4"], "b4": ["a4", "b2", "b6", "c4"],
        "c4": ["b4", "c3", "c5"], "e4": ["e3", "e5", "f4"],
        "f4": ["e4", "f2", "f6", "g4"], "g4": ["f4", "g1", "g7"],
        "c5": ["c4", "d5"], "d5": ["c5", "d6", "e5"], "e5": ["d5", "e4"],
        "b6": ["b4", "d6"], "d6": ["b6", "d5", "d7", "f6"],
        "f6": ["d6", "f4"], "a7": ["a4", "d7"], "d7": ["a7", "d6", "g7"],
        "g7": ["d7", "g4"]}
    
    #List of mills
    MILLS = [["a1", "d1", "g1"], ["b2", "d2", "f2"],
        ["c3", "d3", "e3"], ["a4", "b4", "c4"], ["e4", "f4", "g4"],
        ["c5", "d5", "e5"], ["b6", "d6", "f6"], ["a7", "d7", "g7"],
        ["a1", "a4", "a7"], ["b2", "b4", "b6"], ["c3", "c4", "c5"],
        ["d1", "d2", "d3"], ["d5", "d6", "d7"], ["e3", "e4", "e5"],
        ["f2", "f4", "f6"], ["g1", "g4", "g7"]]
        
    def __init__(self):
        #Initializes points to be spaces
        self.points = {"a1": " ", "d1": " ", "g1": " ",
        "b2": " ", "d2": " ", "f2": " ", "c3": " ", "d3": " ",
        "e3": " ", "a4": " ", "b4": " ", "c4": " ", "e4": " ",
        "f4": " ", "g4": " ", "c5": " ", "d5": " ", "e5": " ",
        "b6": " ", "d6": " ", "f6": " ", "a7": " ", "d7": " ",
        "g7": " "}
        
    def assign_piece(self,player,destination):
        # assigns a player to a point
        self.points[destination] = player
    
    def is_occupied(self, player, position):
        # player is 'X', 'Y' etc. and position is a valid position like 'a1', 'b2' etc.
        # return True if the position 'a1' contains 'X', otherwise return False
        player = "X" if player == "O" else "O"
        if self.points[position]==player:
            bool = True
        else:
            bool = False
        return bool
    
    
    def clear_place(self,destination):
        # clears a point place, effectively removing a player
        self.points[destination] = " "

    def __str__(self):
        """
        Display everything nice and pretty-like.
        This is an ugly function.
        """
        s = "\n"
        s+= "    7 [" + self.points["a7"] + "]------[" + self.points["d7"] + \
              "]------[" + self.points["g7"] + "] \n"
        s+= "    6  | [" + self.points["b6"] + "]---[" + self.points["d6"] + \
              "]---[" + self.points["f6"] + "] |\n"
        s+= "    5  |  | [" + self.points["c5"] + "][" + self.points["d5"] + \
              "][" + self.points["e5"] + "] |  |\n"
        s+= "    4 [" + self.points["a4"] + "][" + self.points["b4"] + "][" + \
              self.points["c4"] + "]   [" + self.points["e4"] + "][" + \
              self.points["f4"] + "][" + self.points["g4"] + "]\n"
        s+= "    3  |  | [" + self.points["c3"] + "][" + self.points["d3"] + \
              "][" + self.points["e3"] + "] |  |\n"
        s+= "    2  | [" + self.points["b2"] + "]---[" + self.points["d2"] +\
              "]---[" + self.points["f2"] + "] |\n"
        s+= "    1 [" + self.points["a1"] + "]------[" + self.points["d1"] + \
              "]------[" + self.points["g1"] + "]\n"
        s+= "       a  b  c  d  e  f  g\n"
        s+= "\n"
        return (s)
    
    
    


board = Board()

BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
        counts the number of mills for the player and returns the count
    """
    count= 0
    player_point_list = []
    for k,v in board.points.items():
        if v == player:
            player_point_list.append(k)
    for mill in board.MILLS:
        if (set(mill)<=set(player_point_list)) == True:
            count += 1
    return count

        
            
def place_piece_and_remove_opponents(board, player, destination):
    """
        count the number of mills, then assigns a point to a spot. If there is
        a point there already an Error is returned. Otherwise the mills count
        is returned again. If the mills is greater the second time a new one
        was created and the player gets to remove a point from the board.
    """

    count1 = count_mills(board,player)
    if board.is_occupied(player, destination) == True:
        print("error: ",board.is_occupied(player, destination))
        raise RuntimeError("Invalid command: Destination point already taken")
        
    else:
        board.assign_piece(player,destination)
    count2 = count_mills(board,player)
    if count2 > count1:
        print("A mill was formed!")
        print(board)
        bool1 = True
        while bool1 == True:
            try:
                remove_piece(board, player)
                bool1 = False
            except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
                    
    
 
#place_piece_and_remove_opponents(board, '1', 'a1')
#print(board)
#place_piece_and_remove_opponents(board, '1', 'a4')
#print(board)
#place_piece_and_remove_opponents(board, '1', 'd7')
#print(board)
#place_piece_and_remove_opponents(board, '1', 'f4')
#print(board)
#place_piece_and_remove_opponents(board, '1', 'f2')
#print(board)
   
def move_piece(board, player, origin, destination):
    """
        calls the place and remove pieace function to place and remove and
        also reomves the original point
    """ 
    if board.points[origin] != player:
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    else:
        adjacent_list = board.ADJACENCY[origin]
        if destination not in adjacent_list:
            if destination not in board.points.keys():
                raise RuntimeError("Invalid command: Not a valid point")
            else:
                raise RuntimeError("Invalid command: Destination is not adjacent")
        else:
            board.clear_place(origin)
            place_piece_and_remove_opponents(board, player, destination)
    
    
#move_piece(board, '1', 'd7', 'a7')
    
def points_not_in_mills(board, player):
    """
        returns a set of points that the player has not in a mill
    """
    player_point_list = []
    for k,v in board.points.items():
        if v == player:
            player_point_list.append(k)
    mill_list = []
    for mill in board.MILLS:
        if (set(mill)<=set(player_point_list)) == True:
            for i in mill:
                mill_list.append(i)
    points_not_in_mills = set(player_point_list) - set(mill_list)
    return points_not_in_mills
    
#points_not_in_mills(board, '1')        
        
def placed(board,player):
    """
        returns a list of points where the players pieces have been placed
    """
    player_point_list = []
    for k,v in board.points.items():
        if v == player:
            player_point_list.append(k)
    return player_point_list
    
def remove_piece(board, player):
    """
        This function checks to see if a point may be reomved. If it can it
        removes it, if not then Error messege is returned
    """
    player = get_other_player(player)
    player_point_list = placed(board,player)
    points = points_not_in_mills(board, player)
    bool = True
    while bool == True:
        remove = input("Remove a piece at :> ")
        if len(remove) != 2:
            raise RuntimeError ("Invalid command: Not a valid point")
        else:
            if remove not in player_point_list:
                
                    raise RuntimeError("Invalid command: Point does not belong to player")
            elif remove not in points:
                if len(points) != 0:
                    raise RuntimeError("Invalid command: Point is in a mill")
                else:
                    board.clear_place(remove)
                    bool = False
            else:
                board.clear_place(remove)
                bool = False

    
#remove_piece(board, '1')   
           
def is_winner(board, player):
    """
        takes the list of points placed for a player. if they have less then 
        3 points they lost and the True bool is returned.
    """
    player = "X" if player == "O" else "O"
    bool = False
    points_list = placed(board,player)
    if len(points_list)<3:
        bool = True
    return bool
   
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"
    
def main():
    #Loop so that we can start over on reset
    while True:
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = Board()
        print(board)
        player = "X"
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent
        
        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            bool1 = True
            while bool1 == True:
                if command.lower() == 'h':
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                if command == 'r':
                    return main()
                try:
                    place_piece_and_remove_opponents(board, player, command)
                    placed_count += 1
                    player = get_other_player(player)
                    bool1 = False
                #Any RuntimeError you raise inside this try lands here
                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
                    break
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
        
        #Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            bool1 = True
            while bool1 == True:
                try:
                    if len(command) != 2:
                        raise RuntimeError("Invalid number of points")
                    move_piece(board, player, command[0], command[1])
                    bool = is_winner(board, player)
                    if bool == True:
                        player = get_other_player(player)
                        print(BANNER)
                        return
                    player = get_other_player(player)
                    bool1 = False
                #Any RuntimeError you raise inside this try lands here
                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
                    break
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

            
if __name__ == "__main__":
    main()
