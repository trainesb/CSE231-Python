    ###########################################################
    #  Computer Project #9
    #
    #   open_file() prompts the user for a file. if the file
    #   can't be opened an error msg is retruned and askes for a
    #   nwe input.
    #
    #   validate_hashtag(s) takes one paramter s.  s is a string which contains
    #   a hashtag from twitter.  if the firsth ch is no a # then the function
    #   returns False. The functin also returns false if the string contains
    #   punctuation, or is shorter the 3 ch in len. If it isnt any of those
    #   then the function returns True.
    #   
    #   get_hashtags(s) takes one parameter s. s is a string that is a hashtag
    #   the function validates s with the validate_hashtag() function. If the 
    #   validation function returns true then then s is added to teh list, if
    #   not then it's not added to the list. The list is returned.
    #   
    #   read_data(fp) takes one paramter fp. fp is the open_file() function
    #   and reads the lines. The function creats a list wiht the username, 
    #   month and hashtags. The hastags is a list which was made by reading
    #   the lines and validating the words if they are a hastag or not. If they
    #   are they are added to the hashtag list. the list of these three were
    #   then added to a list with list for each line and that list was returned
    #
    #   get_histogram_tag_count_for_users(data,usernames) takes two parmaters,
    #   data list from read_data() and usernames which can be a single username
    #   or a list of many. The file collects the hastags for those usernames
    #   and creates a dictionary. The hastag is the key and the count of how
    #   many times it was used is the value. The dict is returned
    #
    #   get_tags_by_month_for_users(data,usernames) takes two parameters, data
    #   which is the list from read_data() and a username or list of usernames.
    #   The function sorts the data by username and removes any not on entered.
    #   It then sorts by date and creats a dict with the date as the key and a
    #   set of hashtags as its value.  The dict is then turned into a set of
    #   tupples added to a list, and the list is returned.
    #
    #   get_user_names(L) takes a data list L from read_data() and collects a 
    #   list of diffrent usernames. Then sorts these usernames alphabetially 
    #   and returns the sorted list.
    #
    #   three_most_common_hashtags_combined(L,usernames) takes two paramters,
    #   L is a dict that is returned by another funvtion and usernames is the 
    #   list of usernames to call that dict for. The function then makes a list
    #   of the three most used hastags and returns it.
    #
    #   three_most_common_hashtags_individuals(data_lst,usernames) takes two
    #   paramters. data_lst which is a dic from another function and a list of
    #   usernmaes. the function runs each username through the data_lst
    #   function to get a dic for each username with their hashtags and count.
    #   The function sorts these by counts and makes the list of the top three.
    #   The top three from each username are aded to the maser_list and sorted 
    #   by count. The top three are returned with (count, hashtag, username).
    #
    #   similarity(data,user1,user2) takes three paramters. data which is
    #   pulled in from open_file(), and two usernames.  The function collects
    #   a list of hashtags both usernames used the past year.  It then compares
    #   each year and counts how many words they used that were simillar 
    #   each month. The function then returned a list with a tupple (month,
    #   count of hashtags similar)
    #
    #   main() The function opens and reads the file with the read_data()
    #   function.  A list of all usernames is made with the get_username
    #   fnction. Prints the top three hastags combined and then the top three
    #   individually. Asks the user for two usernames and finds the similarity
    #   between them. Then asks the user if they want to plot this.
    #
    ###########################################################

'''Skeleton file with all strings for Mimir testing'''

import string, calendar, pylab
from operator import itemgetter

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    '''prompt for file name, open file, return file pointer'''
    bool = False
    while not bool: #if file is not found print error and reprompt
        try:
            filename = input("Input a filename: ") #prompt for file name
            fp = open(filename, "r") #open file
            bool = True
        except FileNotFoundError:
            print("Error in input filename. Please try again.")
    print()
    return fp

def validate_hashtag(s):
    '''if s[0] isnt "#" return false, if there is punctuation in s return
    false. If the length is less then 3 return false, else return true'''
    
    if s[0] != '#':
        return False
    else:
        s = s[1:]
        for i in s:
            if i in string.punctuation:
                return False
        if len(s) < 2:
            return False
    return True

#validate_hashtag("#ff")

def get_hashtags(s):
    '''if s is a valid hashtag then it is added to the list, if not then it's 
    not added, the list is returned'''
    tweet_list = []
    s=s.strip().split()
    for i in s:
        if validate_hashtag(i) == True:
            tweet_list.append(i)
    return tweet_list

#get_hashtags("#tag1 some words, etc. #2, another #tag2")

def read_data(fp):
    '''read the lines in fp and made a list with the username, month, and
    hashtags'''
    data_list = []
    for line in fp:
        line = line.split(',')
        predata_list = []
        predata_list.append(line[0])
        predata_list.append(int(line[1]))
        line = line[2].split()
        hashtag_list = []
        for ch in line:
            if validate_hashtag(ch) == True:
                hashtag_list.append(ch)
        predata_list.append(hashtag_list)
        data_list.append(predata_list)
    return data_list

#read_data(open_file())

def get_histogram_tag_count_for_users(data,usernames):
    '''takes the data list from read_data() and counts how many times a 
    hastag is used for a username or many usernames. returns dict'''
    dict = {}
    list=[]
    for i in data:
        if i[0] in usernames:
            list.append(i)
    for i in list:
        hashtags = i[2]
        for h in hashtags:
            if h not in dict.keys():
                dict[h]=1
            else:
                dict[h]+=1
    return dict
            

#get_histogram_tag_count_for_users(read_data(open_file()),'MSUnews')

def get_tags_by_month_for_users(data,usernames):
    '''takes data and sorts by month, and username. then adds hashtags to a
    set and adds them to a dict with month as its key. turns this dict into 
    a tuplle adds the tupple to a list and returns the list'''
    tags_by_month = [(1,set()),(2,set()),(3,set()),(4,set()),(5,set()),\
                     (6,set()),(7,set()),(8,set()),(9,set()),(10,set()),\
                     (11,set()),(12,set()),]
    L =[]
    for i in data:
        if i[0] in usernames:
            L.append(i)   
    L = sorted(L, key=itemgetter(1))
    for a in L:
        for i in tags_by_month:
            if a[1] == i[0]:
                i[1].update(a[2])
    return tags_by_month

    
#get_tags_by_month_for_users(read_data(open_file()),['WKARnewsroom'])

def get_user_names(L):
    '''takes data list from read_data() and collects all diffrent usernames
    in a list, then sorts alphabetically, and returns the list.'''
    usernames = []
    for i in L:
        if i[0] not in usernames:
            usernames.append(i[0])
    usernames = sorted(usernames)
    return usernames
    
#get_user_names(read_data(open_file()))    

def three_most_common_hashtags_combined(L,usernames):
    '''takes a dic of hashtags used by username and returns a list of the top
    three hastags used'''
    L = get_histogram_tag_count_for_users(L,usernames)
    hashtag_list = []
    for k,v in L.items():
        tup = (v,k)
        hashtag_list.append(tup)
    hashtag_list = sorted(hashtag_list, key=itemgetter(0), reverse=True)
    hashtag_list = hashtag_list[:3]
    return hashtag_list
        

#three_most_common_hashtags_combined(read_data(open_file()),'p')

def three_most_common_hashtags_individuals(data_lst,usernames):
    '''takes a dic of each username entered and sorts them from high to low.
    puts the three high ones from each username in a list and sorts these the
    same. the function then returns a list with the three highest counts, with
    there hashtag and username.'''
    master_list = []
    for i in usernames:
        lst = get_histogram_tag_count_for_users(data_lst,i)
        list = []
        for k,v in lst.items():
            tup = (v,k,i)
            list.append(tup)
        list = sorted(list, key=itemgetter(0), reverse=True)
        list = list[:3]
        for i in list:
            master_list.append(i)
    master_list = sorted(master_list, key=itemgetter(0), reverse=True)
    master_list = master_list[:3]
    return master_list

#three_most_common_hashtags_individuals(read_data(open_file()),"MSUnews, WKAR")
            
def similarity(data,user1,user2):
    '''compares to users each month and counts the number of hashtags both used
    that were the same and returns the list'''
    user2 = [user2]
    user1 = [user1]
    data_list1=get_tags_by_month_for_users(data, user1)
    data_list2=get_tags_by_month_for_users(data,user2)
    list_set1 = []
    list_set2 = []
    list=[]
    for i in data_list1:
        set1=set(i[1])
        list_set1.append(set1)
    for a in data_list2:
        set2=set(a[1])
        list_set2.append(set2)

    for i in range(0,12):
        date = i+1
        if i<len(list_set1):
            set_01 = list_set1[i]
        else:
            break
        if i<len(list_set2):   
            set_02 = list_set2[i]
        else:
            break
        set3 = set_01 & set_02
        tup=(date, set3)
        list.append(tup)
    return list


#similarity(read_data(open_file()),"WKARnewsroom", "WKARnewsroom")
        
def plot_similarity(x_list,y_list,name1,name2):
    '''Plot y vs. x with name1 and name2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")


def main():
    fp = read_data(open_file()) # Open the file Read the data from the file
    usernames = get_user_names(fp) # Create username list from data
    
    # Calculate the top three hashtags combined for all users
    combined = three_most_common_hashtags_combined(fp,usernames)
    # Print them
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    for i in combined:
        print("{:>6d} {:<20s}".format(i[0],i[1]))
    print()
    
    # Calculate the top three hashtags individually for all users
    individually = three_most_common_hashtags_individuals(fp,usernames)
    # Print them
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    for a in individually:
        print("{:>6d} {:<20s} {:<20s}".format(a[0],a[1],a[2]))
    print()
    
    # Prompt for two user names from username list
    print("Usernames: ", ', '.join(usernames))
    
    bool = True
    while bool == True:  # prompt for and validate user names
        user_str = input("Input two user names from the list, comma separated: ")
        user_str = user_str.strip().split(',')
        for i in user_str:
            while i[0] == ' ':
                if i[0] == ' ':
                    i = i[1:]
                
            if i not in usernames:
                print("Error in user names.  Please try again")
                break
            else:
                bool = False
   
    # Calculate similarity for the two users
    user1 = user_str[0]
    user2 = user_str[1].strip()
    sim = similarity(fp,user1,user2)
    # Print them
    print()
    print("Similarities for "+user1+" and "+user2)
    print("{:12s}{:6s}".format("Month","Count"))
    for month in sim:
        length = len(month[1])
        print("{:12s}{:<6d}".format(calendar.month_name[month[0]],length))
    print()
   
    # Prompt to plot or not and plot if 'yes'
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        #create x_list and y_list
        x_list =[]
        y_list =[]
        for month in sim:
            x_list.append(month[0])
            y_list.append(month[1])
        
        plot_similarity(x_list,y_list,user1,user2)

if __name__ == "__main__":
    main()