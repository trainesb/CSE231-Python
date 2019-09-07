# assume a word has at least one vowel
#task the user to input a word
#run the loop until every vowel is coolected or at least 5 consonants
#only collect the constants after the last vowel

#list the VOWELS and set the variable strings to empty
VOWELS="aeiou"

vowels = ""
con = ""
vowel_index =""

#loop will run until vowels = "aeiou" or there are five or more consonants
while len(vowels) != 5 or len(con) < 5:
    
    
    #breaks loop if vowels = "aeiou" or there are five or more consonants
    if len(vowels) == 5:
        break
    elif len(con) >= 5:
        break
    
    #promps user to enter a string and makes it lower case
    word = input("Input a word: ")
    word = word.lower()
    new_word = word
    

    #runs loop until there are no letters left in the word
    while len(new_word) != 0:
        
        #use enumerate to index the ch to be bale to find last vowel
        for i,ch in enumerate(word):
            
            #if the first letter in the word is a vowel...
            if ch in VOWELS:
                
                #if the first letter is not already in variable vowel; add it
                #once letter is added shorten word by one letter
                if ch not in vowels:
                    vowels += new_word[0]
                    vowel_index = i
                    new_word = new_word[1:]


                #if the letter is already in variable vowels just shorten word
                else:
                    new_word = new_word[1:]
                    vowel_index = i
                    
            #if the first letter is not a variable shorten the word
            else:
                new_word = new_word[1:]
        
        #add the slice to the variable consonants     
        consonants = word[(vowel_index + 1):]
        
        #run a lopp checking each ch in consonants to see if the are in con
        while len(consonants) != 0:
            
            #if ch is not in con then add first letter and shorten
            if consonants[0] not in con:
                con += consonants[0]
                consonants = consonants[1:]

            #if first ch is in con then just shorten it
            else:
                consonants = consonants[1:0]

#length of vowels
length_vowels = str(len(vowels))
#length of consonants
length_con = str(len(con))
        
print("\n"+"="*12)               
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants","length"))
print("{:8s}{:7s} | {:12s}{:7s}".format(vowels,length_vowels,con,length_con))