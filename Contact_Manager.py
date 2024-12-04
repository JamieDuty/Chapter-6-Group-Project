#Contact Manager
import os

#coffee shop menu
def coffee_shop_menu():
    #coffee shop accepts no arguments
    #it displays and returns a menu choice
    
    #display menu
    input("Print any key to display menu: ")
    print('\nWelcome to Caffeine Overload Inventory Control System. Please choose an inventory option.')
    print('1) Add a record')
    print('2) Modify a record')
    print('3) Delete a record')
    print('4) Display all saved records')
    print('5) Search for a record')
    print('6) Exit')

    choice = input('Inventory option: ')
    
    return choice

def main(): 
    #contact manager accepts no arguments
    #it calls coffee_shop_menu to display a menu to the user
    #and calls each function according to the user input
    
    #prime the loop
    choice = int(coffee_shop_menu())
    
    #validate menu choice
    while choice < 1 or choice > 6:
        print("Invalid choice!")
        choice = int(coffee_shop_menu())
        
    #loop to call the desired function
    while choice != 6:
        if choice == 1:
            write_coffee()
        elif choice == 2:
            modify_coffee()
        elif choice == 3:
            delete_coffee()
        elif choice == 4:
            read_coffee()
        elif choice == 5:
            search_coffee()
        choice = int(coffee_shop_menu())
    print("Thank you for using the Caffeine Overload Inventory Control System. Have a great day.")