    ###########################################################
    #  Computer Project #07
    #
    #   open_file() prompts the user for a file. if the file
    #   can't be opened an error msg is retruned and askes for a
    #   nwe input.
    #
    #   read_ip_location(file) takes a file and reads the lines in the file.
    #   slices the line into proper variables. Takes the start_ip and end_ip
    #   variable and splits at each '.' and adds leadin 0 so that all are 3
    #   charachters in length. Makes a tupple for each and adds the tupples
    #   to a list which is returned.
    #
    #   read_ip_attack(file) takes a file and reads it, adding '.xxx' to the
    #   end of each line and assigns it to a variable.  it then adds '.000'
    #   to the end of the line and again splits and adss leading zeros.  Then
    #   puts these two in a tupple and adds the tupple to a list.
    #
    #   read_country_name(file) takes a file of countrys and their codes.
    #   split the line into code and name, then puts the two in a list
    #   and returns it.
    #
    #   locate_address(ip_list, ip_attack) takes the list from read_ip_location
    #   and a single ip for ip_attack.  Then goes thru the list and if the
    #   ip_attack is between the start and end ip it returns that countries
    #   code.
    #
    #   get_country_name(country_list, code) takes the country_list(dict) from
    #   read_country_name and the code is a single code. The function compares
    #   the code to each line[0] in each tupple. If its a match the full name
    #   is returned.
    #
    #   bar_plot(count_list, countries) takes count_list and countries from the
    #   top 10 attacks list made in the main() function. Uses these two to make
    #   a histogram.
    #
    #   main() askes the user to enter files for each of the three main
    #   functions that return lists and the one that returns a dict.  Then asks
    #   user if they want to see all the data.  if answer is yes then
    #   private IP and the full country name is displayed for each IP. The
    #   function then goes thru all attack IP and gets their country code.
    #   the function keeps a count of how many times the code came up.  It then
    #   lists the code from most to least and in opposite alphabetical oorder.
    #   lastly the program asks if the user would like to plot. If the users
    #   answer is yes then the bar_plot() function is ran.
    ###########################################################

import csv
import pylab
from operator import itemgetter

def open_file(message):
    '''prompt for file name, open file, return file pointer'''
    bool = False
    while not bool: #if file is not found print error and reprompt
        try:
            filename = input(message) #prompt for file name
            fp = open(filename, "r") #open file
            bool = True
        except FileNotFoundError:
            print("File is not found! Try Again!")
    return fp

#open_file('hey')
           
def read_ip_location(file):
    '''reads line in file from opne_file(). strips and splits at each ','
    then splits it up into start_ip, end_ip, and country code. for start
    and end ip the program splits at each '.' and adds 0 to the front to make
    it three charachters long.  puts the start_ip, end_ip, and country code in
    a tupple and appends the tupple to the list and returns the list'''
    country_code = ''
    ip_location_list = []
    file = csv.reader(file)
    for line in file:
        country_code = line[2]
        og_start_ip = line[0]
        og_end_ip = line[1]
        og_start_ip = og_start_ip.split('.')
        og_end_ip = og_end_ip.split('.')
        start_ip = ''
        end_ip = ''
        
        for i in og_start_ip:
            i = i.zfill(3)
            start_ip += i
        start_ip = int(start_ip)
        
        for i in og_end_ip:
            i = i.zfill(3)
            end_ip += i
        end_ip = int(end_ip)
        tup = (start_ip, end_ip, country_code)
        ip_location_list.append(tup)
    return ip_location_list

#dbip-country.csv
#read_ip_location(open_file('input: '))


def read_ip_attack(file):
    '''reads file from open_file(). sets ip_priv to the line in the file and
    adds '.xxx' to the end of each. line then adds '.000' to the end of each
    ip. The program then splits at each '.', and adds leadin 0 till the length
    is 3. then adds them to ip and makes it an int. creates tupple with
    (ip, ip_priv) and adds each to a list. returns list'''
    ip_attack_list = []
    for line in file:
        ip_priv = line.strip() + '.xxx'
        line = line.strip() + '.000'
        line = line.split('.')
        ip = ''
        for i in line:
            i = i.zfill(3)
            ip += i
        ip = int(ip)
        tup = (ip, ip_priv)
        ip_attack_list.append(tup)
    return ip_attack_list

#2017-09-27-attacks-small.txt
#read_ip_attack(open_file('hey')) 

def read_country_name(file):
    '''reads file from open_file(). strips each line in the file and splits at
    every ';'. takes list after split and assigns country_code and full_name
    to proper values.  adds the two to a list and returns list.'''
    country_name_list = []
    for line in file:
        line = line.strip().split(';')
        country_code = line[1]
        full_name = line[0]
        tup = (country_code, full_name)
        country_name_list.append(tup) 
    return country_name_list

#country_names.txt 
#read_country_name(open_file('hey')) 
    
def locate_address(ip_list, ip_attack):
    '''takes ip_list from the list returned in read_ip_location(). sets the
    variable country_code to an empty string. reads each tupple in the list.
    if the ip_attack given is between the start_ip and end_ip then returns
    the country code.'''
    for line in ip_list:
        country_code = ''
        if line[0] <= ip_attack <= line[1]:
            country_code = line[2]
            return country_code
        else:
            continue
            
#dbip-country.csv
#locate_address(read_ip_location(open_file('hey')), 128015000)

def get_country_name(country_list, code):
    '''Takes country_list which is the list returned from read_country_name().
    reads thru the lines and if the code in the tupple matches code given, the
    function returns the full name.'''
    for line in country_list:
        if line[0] == code:
            full_name = line[1]
        else:
            continue
    return full_name

#country_names.txt 
#get_country_name(read_country_name(open_file('hey')), 'US')
    
def bar_plot(count_list, countries):
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    '''opens a file for three of the functions and saves the list and dict
    that they return.  uses the saved data to display all info if requested.
    also runs all the attack_data and finds the country of origins. Keeps a 
    list of the countries with a count and prints from high to low'''
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)
    print()
    display_all = input("Do you want to display all data? ")
    display_all = display_all.lower()
    if display_all == 'yes':
        for line in attack_data:
            ip_priv = line[1]
            attack_ip = line [0]
            code = locate_address(ip_data, attack_ip)
            full_country_name = get_country_name(country_data, code)
            print("The IP Address: {:18s} originated from {:>0s}".format(\
                  ip_priv, full_country_name))

    print()
    attack_dict = {}
    for line in attack_data:
        ip_attack = line[0]
        attack_country_code = locate_address(ip_data, ip_attack)
        if attack_country_code not in attack_dict:
            attack_dict[attack_country_code] = 1
        else:
            attack_dict[attack_country_code] += 1
            
    list_data = []
    for key, value in attack_dict.items():
        tup = (key, value)
        list_data.append(tup)
    new_list_data = list_data
    new_list_data.sort(reverse=True)
    new_list_data = sorted(list_data, key=itemgetter(1), reverse = True)
    print("Top 10 Attack Countries")
    print("{:7s} {:>6s}".format("Country","Count"))
    count_list = []
    countries = []
    for item in new_list_data[:10]:
        count_list.append(item[1])
        countries.append(item[0])
        print("{:7s} {:>6d}".format(item[0],item[1]))
    answer = input("\nDo you want to plot? ")
    answer = answer.lower()
    if answer == 'yes':
        bar_plot(count_list, countries)
    
if __name__ == "__main__":
    main()