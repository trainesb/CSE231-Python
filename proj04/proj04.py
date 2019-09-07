    ###########################################################
    #  Computer Project #4
    #
    #   get_ch() function prompts user for ch
    #   if ch is longer then one ch error msg
    #   if one ch long or empty returns
    #
    #   find_state)state, ch) function takes ch from get_ch()
    #   it then finds its state final at 4 or 5
    #
    #   main() calls in get_ch and collects the ch
    #   also finds the state of each charecter
    #   starting at state one with the first and increasing
    #   stops collecting ch when return is entered
    #   if its in state 4, user is laughing
    #   if state 5, user is not laughing
    #   
    ###########################################################
#promps for a ch and returns it if its one ch or a empty string
def get_ch():

    # prompt for a ch
    ch = input("Enter a character or press the Return key to finish: ")
      
    #if ch is not a emptry str or one ch then print error and repromp in loop
    # exits loop when ch is one ch or less in length
    if len(ch) > 1:
        while len(ch) > 1:
            # in case of invalid input, print the following error message
            print("Invalid input, please try again.")
            ch = input("Enter a character or press the Return key to finish: ")
        return ch
    #if the ch is one ch or an empty string return it
    else:
        return ch
#finds the state of ch and retuns it
def find_state(state, ch):
    #starts at state one
    if state == 1:
        if ch == 'h': #if the first ch is h move to state 2
            state +=1
        else: #esle its wrong and we move to state 5
            state = 5
    elif state == 2: #if we are at state 2
        if ch == 'a' or 'o': #the 2nd ch is an 'a' or 'o' then move to 3rd
            state += 1
        else: #if its not a 'a' or 'o' move to 5
            state = 5
    elif state == 3: #if we are in state 3
        if ch == '!': # the 3rd ch is a '!' we ared done and move to 4
            state = 4
        elif ch == 'h': #if its a 'h' move back to 2 for testing
            state -= 1
        else:
            state = 5# if not any above then its wrong and goes to state 5
    elif state == 4: #if we are in state 4 and another ch is eneterd go to 5
        state = 5
    return state
#calls in in both functions and keeps track of ch and state
def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")
    
    #calls in ch from the get_ch() function
    ch = get_ch()
    #empty string to track ch entered and state starts at 1
    string = ""
    state = 1
    #loop the ch until retrun is eneterd
    while ch != "":

        #calls in find_state() function to track the state from each ch
        state = find_state(state, ch)
        #adds ch to string and promps for another
        string += ch     
        ch = get_ch()
   
    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    
    #if final state is 4, print you are laughing
    if state == 4:
        return print("You are laughing.")
   #if final state isn't 4, user isn't laughing
    else:
        return print("You are not laughing.")

start = main()
