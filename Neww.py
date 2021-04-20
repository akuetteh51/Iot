# project: Assignment Guide
# Author: Michael Nana Kwame Akuetteh
#  date : 14/12/2020

# A painting company has determined that for every 115 square 
# feet of wall space,one gallon
# of paint and eight hours of labor will be required.
#  The company charges $20.00 per hour for
#  labor.Write a program that asks the user to enter the
#  square feet of wall space to be 
#  painted and the price of the paint per gallon. 
# The program should display the following data:

#  1. The number of gallons of paint required
#  2. The hours of labor required
#  3. The  cost of the paint
#  4. The  labor charges
#  5. The  total cost of the paint job  

######################## Logics ,maths required and data,keywords or variables ############################ 
# Square_ft
# num_Of_gallon
# Cost_of_paint
# Labor_charges
# Total_Cost
# Price
# Hour(s)
 
#############################  logics and calculations ###################################
# 115 square feet =1gallon and 8 hours
# Charge per hour =$20.00
# the logic should be all input must be specified if not 
# there should an else or else if to tell the user to enter the 
# required input
#  number of gallons =square_feet divided by 115
# number of hours =number of gallons times 8
# Cost of paint = number of paint times price of 1 gallon
# charge_for_painting = number of hours * 20.00
# Total_cost = Charge_for_painting + cost of paint

############################### code ##########################





while True:
    print("Enter the square Feet of wall space to be painted: ")
    Square_ft=int(input("=>"))
    print("price of paint per gallon ($): ")

    Price=int(input("=>"))
    # function for to display data
    def Data():
            print("____________________________________DATA________________________________________")
            print(f"Square feet of wall: {Square_ft}")
            print(f"Price of paint per gallon ($): {Price}")
            num_Of_gallon=Square_ft/115
            print(f"number of paint(s) required {num_Of_gallon}")
            hours = num_Of_gallon * 8.0
            print(f"Hour(s) required for this painting is: {hours}")
            Cost_of_paint=num_Of_gallon*float(Price)
            print(f"Cost of paint is: {Cost_of_paint}")
            Labor_charges=hours*20.00
            print(f"Charge for workdone is: {Labor_charges}")

            Total_Cost=Labor_charges+Cost_of_paint
            print(f"Total cost for painting is:{Total_Cost}")
            print("_____________________________________________________________________")
             

        

    if(Price !=0 and Square_ft !=0):
        Data()
        print("press 'n' to start or 'q' to exit")
        ls=input("=>")
        if (ls=='n'):
            continue
        elif (ls=='q'):
            print("__________________________________________________________________________")
            break
        
            
        

    elif (Price <=0 or Square_ft <=0 ):

        print("All input required \n Try Again")
        print("_____________________________________________________________________")
        


