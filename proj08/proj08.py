    ###########################################################
    #  Computer Project #8
    #
    #   open_file() prompts the user for a file. if the file
    #   can't be opened an error msg is retruned and askes for a
    #   nwe input.
    #
    #   update_dictionary() takes four paramters: dicitonary, year,
    #   hurricane_name, and data. If the year is in the dictionary then the
    #   function looks to see if the hurricane_name is also in the value for
    #   the year.  If it is it appends data to it, if it is not it adds it.
    #   returns the dictionary
    #
    #   create_dicitonary() takes one paramter the fp from the open_file
    #   function. reads the line and splits each line into its perpective
    #   part. Calls in update_dicitonary() function to update the lines to
    #   it. returns the dicitonary.
    #
    #   display_tbale() takes two parameters dictionary, and year. The 
    #   function sorts the dictionary by windspeed, then lat then lon.
    #   It then prints all the huricanes for that year with the highest wind
    #   speed, date and coordinates
    #
    #   get_years() takes one paramter, a dicitonary. It sorts the dicitonarys
    #   years and gets the first (lowest year) and last (max year). puts these
    #   two in a tupple and returns them.
    #
    #   prepare_plot() takes two paramters, a dicitonary and a year.
    #   it sorts the dicitonarys by name for that year and creates a list of
    #   the names, coordiantes (list of list), and max wind speed. The function
    #   puts them in a tupple and returns the tupple.
    #
    #   plot_map() take the data and create a map of the
    #   hurricane paths. plot_wind_chart() plots a chart of the huricanse max
    #   wind speed on a chart that showes what catagory it is considered.
    #
    #   main() calls the other functions and runs a loop untill you want to
    #   exit the program.
    #   
    ###########################################################

import pylab as py
from operator import itemgetter

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



def update_dictionary(dictionary, year, hurricane_name, data):
    '''takes a dcitonary and data from the file and puts them in their 
    correct places in the dicitonary'''
    if year not in dictionary.keys():
        dictionary[year] = {hurricane_name:[data]}
    elif year in dictionary.keys():
        if hurricane_name not in dictionary[year].keys():
            dictionary[year][hurricane_name]=[data]
        else: 
            dictionary[year][hurricane_name].append(data)
    return dictionary
        
        
        
    
def create_dictionary(fp):
    '''reads the file and puts content from file into a dicitonary
    using teh update_dictionary() function'''
    dictionary = {}
    for line in fp:
        line = line.strip().split()
        year = line[0]
        hurricane_name = line[1]
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        try:
            wind = float(line[6])
        except ValueError:
            wind = 0
        try:
            pressure = float(line[7])
        except ValueError:
            pressure = 0
        data = (lat, lon, date, wind, pressure)
        update_dictionary(dictionary, year, hurricane_name, data)
    return dictionary



#create_dictionary(open_file())

def display_table(dictionary, year):
    '''Takes dicitonary and prints all names for that year with the data for
    the max wind speed'''
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name","Coordinates",\
          "Wind Speed (knots)","Date"))
    L = []
    for h in dictionary[year].keys():
        dictionary[year][h]=sorted(dictionary[year][h], key=itemgetter(1),\
                  reverse=True)
        dictionary[year][h]=sorted(dictionary[year][h], key=itemgetter(0),\
                  reverse=True)
        dictionary[year][h]=sorted(dictionary[year][h], key=itemgetter(3),\
                  reverse=True)
        name = h
        coor1 = dictionary[year][h][0][0]
        coor2 = dictionary[year][h][0][1]
        wind = dictionary[year][h][0][3]
        date = dictionary[year][h][0][2]
        tup = (name, coor1, coor2, wind, date)
        L.append(tup)
    L.sort()
    for i in L:
        print("{:15s}( {:.2f},{:.2f}){:>20.2f}{:>15s}".format(i[0],i[1],i[2],\
              i[3],i[4]))



#display_table(create_dictionary(open_file()),'2017')

def get_years(dictionary):
    '''sorts the key in the dicitionary from small to large, and returns
    a tupple with the min_year and max_year'''
    years = sorted(k for k,v in dictionary.items())
    min_year = years[0]
    max_year = years[-1]
    tup = (min_year, max_year)
    return tup
        
#get_years(create_dictionary(open_file()))
        
def prepare_plot(dictionary, year):
    '''takes dictionary and sorts by name, then makes a list for names, 
    coordinates, and max wind speed and returns them all'''
    names = []
    coor = []
    coordinates = []
    name = []
    speed = []
    for h in dictionary[year].keys():
        dictionary[year][h]=sorted(dictionary[year][h], key=itemgetter(3),\
                  reverse=True)
        max_speed=dictionary[year][h][0][3]
        coor = []
        for i in dictionary[year][h]:
            x = i[0]
            y = i[1]
            t = (x,y)
            coor.append(t)
        coor =sorted(coor, key=itemgetter(1))
        coor =sorted(coor, key=itemgetter(0))
        names.append((h,coor, max_speed))
        names = sorted(names, key=itemgetter(0))
    for element in names:
        name.append(element[0])
        coordinates.append(element[1])
        speed.append(element[2])
        tup = (name, coordinates, speed)
    return tup

    
    # create everything that is required for plotting
    #return names, coordinates, max_speed

#prepare_plot(create_dictionary(open_file()), '2017')
   
def plot_map(year, size, names, coordinates):
    '''plots the hurricane map with each hurricane'''
    
    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    # Set the corners of the map to cover the Atlantic Region
    xshift = (50,190) 
    yshift = (90,30)
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude+xshift[0],max_longitude-xshift[1]))
    py.ylim((-max_latitude+yshift[0],max_latitude-yshift[1]))
	
    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i/size) for i in range(size)]
    
    
    # plot each hurricane's trajectory
    for i,key in enumerate(names):
        lat = [ lat for lat,lon in coordinates[i] ]
        lon = [ lon for lat,lon in coordinates[i] ]
        py.plot(lon,lat,color=colors[i],label=key)
    

     # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0.,-0.5,1.,0.102),loc=0, ncol=3,mode='expand',\
              borderaxespad=0., fontsize=10)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show() # show the full map


def plot_wind_chart(year,size,names,max_speed):
    '''plots the wind chart'''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}"\
                .format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    

def main():
    '''calls other functions and runs a lopp until the user wants to 'quit' the
    program'''
    dictionary = create_dictionary(open_file())
    year_tup = get_years(dictionary)
    min_year = year_tup[0]
    max_year = year_tup[1]
    print("Hurricane Record Software")
    print("Records from {:4s} to {:4s}".format(min_year, max_year))
    year = input("Enter the year to show hurricane data or 'quit': ")
    while year != 'quit':
        if not (min_year <= year <= max_year):
                print("Error with the year key! Try another year")
                year=input("Enter the year to show hurricane data or 'quit': ")
                continue
        
        else:
            display_table(dictionary, year)
            answer = input("\nDo you want to plot? ")
            if answer.lower() == 'yes':
                names, coordinates, max_speed = prepare_plot(dictionary, year)
                size = len(names)
                plot_map(year, size, names, coordinates)
                plot_wind_chart(year, size, names, max_speed)
        year = input("Enter the year to show hurricane data or 'quit': ")
        year = year.lower()
        continue


    
if __name__ == "__main__":
    main()