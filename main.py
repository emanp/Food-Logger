#Author: Emanuelle Pelayo
#Date: April 7th, 2024
#CS457 HW #6
#Food Logger

import datetime
from Entry import Entry
        
def main():
    
    entryList = [] #list that will hold the entries 
    
    while True:
        userOption = int(input("Press 1 to log Food \nPress 0 to EXIT \n"))
        
        match userOption:
            case 1:
                
                #get info from user
                food = str(input("Enter Food: "))
                amountOfFood = int(input("Quantity: "))
                year = int(input("Enter a year: "))
                month = int(input("Enter a month: "))
                day = int(input("Enter a day: "))
                dateEaten = datetime.date(year, month, day)
                
                #put that info in a single entry and add it to a list of entries
                #also to the new table
                entry1 = Entry(food, amountOfFood, dateEaten)
                
                #Once added, let the user know
                print ("-----Logged!-----")
            
            case 0: 
                break
    
            case _: #edge cases
                print ("Enter a valid option...")
                continue
    
    ...


if __name__ == "__main__":
    main()



        
        
        
        
