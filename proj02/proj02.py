#asks user to input a price and payment amount
#given a specific number of change the program will..
#tell the least amount of change to give to the customer

# purchase price and payment will be kept in cents
#asume we have 10 of each change
quarters = 10
dimes = 10
nickels = 10
pennies = 10

#change due start
Quarters = 0
Dimes = 0
Nickels = 0
Pennies = 0

#print this msg on start
print("\nWelcome to change-making program.")

#print the stock...
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

#have the user enter a price in xx.xx chnage to a foalt or if q is enterd quit
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
if in_str != 'q':
    in_float = float(in_str)
    in_int = int(in_float*100)

#if the price inputed is negative display error and ignore
if in_int < 0:
    print("Error: purchase price must be non-negative.")
    #print the stock...
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    if in_str != 'q':
        in_float = float(in_str)
        in_int = int(in_float*100)
    
#prompt for amount paid
paid = int(float(input("Input dollars paid (int): "))*100)

#if paid is less then price print error and ignore
if in_int > paid :
    print("Error: insufficient payment.")
    paid = int(float(input("Input dollars paid (int): "))*100)



#find the change due
change_due = paid - in_int

while in_str != 'q':
    
    #if paid is same as price print...
    if in_int == paid:
        print("No change.")
        #print the stock...
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        #if a num is enterd conver to float if q is then stop
        if in_str != 'q':
            in_float = float(in_str)
            in_int = int(in_float*100)
        else:
            break
        in_float = float(in_str)
        in_int = int(in_float*100)
        paid = int(float(input("Input dollars paid (int): "))*100)
        #reset the chnage due and coins to 0
        Quarters = 0
        Dimes = 0
        Nickels = 0
        Pennies = 0
        change_due = paid - in_int
    
    
    #if not enough change print error
    elif change_due > ((quarters*25) + (dimes*10) + (nickels*5) + pennies):
        print("Error: ran out of coins.")
        break
    
    
    #use quarters first
    elif quarters != 0 and change_due > 24 :
        change_due -= 25
        quarters -= 1
        Quarters += 1
    
    #then dimes
    elif dimes != 0 and change_due > 9:
        change_due -= 10
        dimes -= 1
        Dimes += 1
    
    #then nickels
    elif nickels != 0 and change_due > 4:
        change_due -= 5
        nickels -= 1
        Nickels += 1
    
    #pennies
    elif pennies != 0 and change_due != 0:
        change_due -= 1
        pennies -= 1
        Pennies += 1
    
    #when change is due print the amount of each but only those used
    elif change_due == 0:
        print("Collect change below: ")
        if Quarters > 0:
            print("Quarters:", Quarters)
        if Dimes > 0:
            print("Dimes:", Dimes)
        if Nickels > 0:
            print("Nickels:", Nickels)
        if Pennies > 0:
            print("Pennies:", Pennies)
       
        #print the stock...
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    
    
        #ask for new price and quit if q is enterd
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        if in_str != 'q':
            in_float = float(in_str)
            in_int = int(in_float*100)
        else:
            break
        paid = int(float(input("Input dollars paid (int): "))*100)
        Quarters = 0
        Dimes = 0
        Nickels = 0
        Pennies = 0
        change_due = paid - in_int

    
    

