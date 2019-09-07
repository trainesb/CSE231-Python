    ###########################################################
    #  Computer Project #5
    #
    #   open_file() prompts the user for a file. if the file
    #   can't be opened an error msg is retruned and askes for ne
    #   input.
    #
    #   revenue(num_sales, sale_price) takes the num_sales 
    #   multiplied by the sale_price to get the revenue
    #
    #   cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    #   takes the advertising total (number of ads multiplied by ad price)
    #   adds to the production total (number of slaes * production cost)
    #
    #  calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
    #   calls in the revenue function as well as the cost_of_goods_sold
    #   function. Then calculates the ROI by taking the
    #   (revenue - cost_of_goods_sold)/(cost_of_goods_sold)
    #
    #   main() opens the file slices the file at each diffrent data point
    #   for each line in the file and caluclaets the ROI. Then tracks the 
    #   name of the prodcuts and if they have the same product name the
    #   program compares the ROI and sales and makes adjustments if its larger.
    #   if the prodict name chnages then it prints the total for that product
    #   and resets
    #   
    ###########################################################

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
    
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    revenue = num_sales * sale_price
    return revenue

def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    cost_of_stuff_sold = (num_ads*ad_price) + (num_sales * production_cost)
    return cost_of_stuff_sold

def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    a = revenue(num_sales, sale_price)
    cost_of_good_sold = cost_of_goods_sold(num_ads, ad_price, num_sales,\
                                           production_cost)
    ROI = (a - cost_of_good_sold)/cost_of_good_sold
    return ROI

def main():

    ## open the file
    file = open_file()
    ## Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    ## read the file
    ##   extract the data 


    biggest_ROI = 0
    biggest_roi_type = ''
    max_sales = 0
    max_sales_type = ''
    product_new = ''
    for line in file:

        product = line[:27].strip()

        type_product = line[27:55].strip()

        num = int(line[55:63].strip())

        cost = float(line[63:71].strip())

        sales = int(line[71:79].strip())

        sale_price = float(line[79:87].strip())

        production_cost = float(line[87:95].strip())

        roi = calculate_ROI(num, cost, sales, sale_price, production_cost)

        #if the products name is the same as the others compare them
        if product_new == product:
            if roi > biggest_ROI: #if the new ROI is larger replace it
                biggest_ROI = roi
                biggest_roi_type = type_product
            if sales > max_sales: #if the new max sale is larger relplace it
                max_sales = sales
                max_sales_type = type_product
        elif product_new == '': #if its the first product set that as the maxs
            biggest_ROI = roi
            biggest_roi_type = type_product
            max_sales = sales
            max_sales_type = type_product
        else: #if they dont match print the products data
            print(product_new)
            print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
            print("  {:27s}{:>11d}".format(max_sales_type,max_sales))
            print()
            print("  {:27s}{:>11s}".format("Best ROI","percent"))
            print("  {:27s}{:>11.2f}%".format(biggest_roi_type,biggest_ROI))
            biggest_ROI = roi
            biggest_roi_type = type_product
            max_sales = sales
            max_sales_type = type_product

        product_new = product
    #switch the product name and compare the last product with the previous
    if roi > biggest_ROI:
        biggest_ROI = roi
        biggest_roi_type = type_product
    if sales > max_sales:
        max_sales = sales
        max_sales_type = type_product
    print()
    print(product_new)
    print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    print("  {:27s}{:>11d}".format(max_sales_type,max_sales))
    print()
    print("  {:27s}{:>11s}".format("Best ROI","percent"))
    print("  {:27s}{:>11.2f}%".format(biggest_roi_type,biggest_ROI))
            
            
    ##   print each product's best selling ad sales number, and best ROI
    ##   Here are two print lines to assit with formatting to match Mimir tests
    ##   print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    ##   print("  {:27s}{:>11s}".format("Best ROI","percent"))


if __name__ == "__main__":
    main()