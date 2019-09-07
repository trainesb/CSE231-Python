    ###########################################################
    #  Computer Project #6
    #
    #   open_file() prompts the user for a file. if the file
    #   can't be opened an error msg is retruned and askes for a
    #   nwe input.
    #
    #   read_file(fp) takes the file pointer and puts the data from
    #   the line in its proper variable. Those variables go into tuples
    #   and the tuples into data_list which is retunred
    #
    #   extraxt_data() takes the data_list and a inputed state
    #   it goes thru the data_list and if the state matches the same
    #   state that was inputed that tuple is added to a new list called
    #   state_list
    #
    #   compute_usage() takes the state_list and breaks each line
    #   into its variable and then computes some other numbers. it then
    #   adds these variables and new numbers into a new tuple and adds
    #   the tuples to a list called state_usage_list
    #
    #   display_data takes the data from compute_usage() and prints
    #   it in a formatted form.
    #
    #   plot_water_usage takes data_list and a title for a pie chart, and
    #   creates a pie chart with the catagories given in the global USERS list
    #
    #   main() calls all the functions and validates the state entered.
    #   
    ###########################################################

import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]

def open_file():
    '''prompt for file name, open file, return file pointer'''
    bool = False
    while not bool: #if file is not found print error and reprompt
        try:
            filename = input("Input a file name: ") #prompt for file name
            fp = open(filename, "r") #open file
            bool = True
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
    return fp

    
def read_file(fp):
    '''takes fp and slices data into proper categories, if there is no value\
    then it is equal to 0'''
    data_list = []
    fp.readline()
    for line in fp:
        line = line.strip()
        line = line.split(',')
        state = line[0]

        county = line[2]
        try:
            population = (float(line [6]))*1000
        except ValueError:
            population = 0
        try:
            fresh_water_usage = float(line [114])
        except ValueError:
            fresh_water_usage = 0
        try:
            salt_water_usage = float(line[115])
        except ValueError:
            salt_water_usage = 0
        try:
            water_usage_public = float(line[18])
        except ValueError:
            water_usage_public = 0
        try:
            water_usage_domestic = float(line[26])
        except ValueError:
            water_usage_domestic = 0
        try:
            water_usage_industrial = float(line[35])
        except ValueError:
            water_usage_industrial = 0
        try:
            water_usage_irrigation = float(line[45])
        except ValueError:
            water_usage_irrigation = 0
        try:
            water_usage_livestock = float(line[59])
        except ValueError:
            water_usage_livestock = 0
        tup = (state, county, population, fresh_water_usage, salt_water_usage,\
               water_usage_public, water_usage_domestic, water_usage_industrial\
               , water_usage_irrigation, water_usage_livestock)
        data_list.append(tup)
    return data_list


  
    
def extract_data(data_list, state):
    '''looks at the first idex of every tup, if same as state then add \
    to the list, otherwise skip the tuple and go to the next'''
    state_list = []
    for i in data_list:
        if i[0] == state:
            state_list.append(i)
        else:
            continue
    return state_list
  
def compute_usage(state_list):
    '''takes the state list and computes the total water used and water\
    used per person and creates a tupple'''
    state_usage_list = []
    for line in state_list:
        county = line[1]
        population = line[2]
        total_water_used = line[3] + line[4]
        fresh_water_per = line[3] / line[2]
        tup = (county, population, total_water_used, fresh_water_per)
        state_usage_list.append(tup)
    return state_usage_list
             

def display_data(state_list, state):
    '''takes the tuple from compute_usage() and prints it'''
    state_usage_list = compute_usage(state_list)

    for line in state_usage_list:
        print("{:22s} {:>22,.0f} {:>22.2f} {:>22.4f}".format(line[0], \
              line[1], line[2], line[3]))
    

    

def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.

        This function is provided by the project.
    '''

    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in some_list:

        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x/total * 100,2) for x in y] # computes the percentages.

    color_list = ['b','g','r','c','m']
    pylab.title(plt_title)
    pylab.pie(y,labels=USERS,colors=color_list)
    pylab.show()
    #pylab.savefig("plot.png")  # uncomment to save plot to a file
    
def main():
    '''calls in the other functions, asks for a state input and validates\
    prints data and asks if you want to make a pie chart'''
    print("Water Usage Data from the US and its States and Territories.\n")
    data_list =  read_file(open_file())     
   
    state = input("\nEnter state code or 'all' or 'quit': ")
    state = state.upper()

    while state != 'QUIT':
        

        if state == 'ALL':
            title = "Water Usage in " + state + " for 2010"
            header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
                  "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")
    
            print("{:^88s}".format(title))
            print(header)
            
            display_data(data_list,state)

           
        elif state not in STATES:
            print("Error in state code.  Please try again.")
            state = input("\nEnter state code or 'all' or 'quit': ")
            state = state.upper()
            continue
        else:
            title = "Water Usage in " + state + " for 2010"
            header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
                  "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")
    
            print("{:^88s}".format(title))
            print(header)
            display_data(extract_data(data_list,state),state)
        
        answer = input("\nDo you want to plot? ")
        if answer == 'yes':
            plt_title = input("Input a plot title: ")
            plot_water_usage(data_list, plt_title)
            
            
        state = input("\nEnter state code or 'all' or 'quit': ")
        state = state.upper()
 
   


if __name__ == "__main__":
    main()
