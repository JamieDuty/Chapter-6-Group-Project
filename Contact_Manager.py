#Contact Manager
import os

#coffee shop menu
def contact_manager():
    #contact manager accepts no arguments
    #it displays and returns a menu choice
    
    #display menu
    input("Print any key to display menu: ")
    print('Choose contact option.')
    print('1) Add a record')
    print('2) Modify a record')
    print('3) Delete a record')
    print('4) Display all saved records')
    print('5) Search for a record')
    print('6) Exit')

    choice = input('Contact Option: ')
    
    return choice
#---------------------------------------------------------------------------------------------------
def main(): 
    #contact manager accepts no arguments
    #it calls contact_manager to display a menu to the user
    #and calls each function according to the user input
    
    #prime the loop
    choice = int(contact_manager())
    
    #validate menu choice
    while choice < 1 or choice > 6:
        print("Invalid choice!")
        choice = int(contact_manager())
        
    #loop to call the desired function
    while choice != 6:
        if choice == 1:
            write_contact()
        elif choice == 2:
            modify_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            read_contact()
        elif choice == 5:
            search_contact()
        choice = int(contact_manager())
    print("Thank you for using the Contact Manager System. Have a great day.")
#-------------------------------------------------------------------------------------------------
def write_contact(): #Option 1
    #write_contact accepts no arguments
    #it opens the file contact.txt to append
    #it loops while the user wants to continue entering records
    #it prompts the user for the coffee description and number of pounds
    #the user should be prompted if they want to continue
    
    #prime the loop, open the file to append, display the header
    another = 'y'
    coffee_file = open('contact.txt', 'a')
    
    #loop to get the records
    while another.lower() == 'y':
        print("Enter the following contact data:\n")
        name = input("Name: ")
        address = input("Street Address: ")
        phone = input("Phone Number: ")
        email = input("Email Address: ")
        
        #append the information to the file
        contact_file.write(name + "\n")
        contact_file.write(address + "\n")
        contact_file.write(phone + "\n")
        contact_file.write(email + "\n")
       
        #prompt for another entry
        another = input("\nDo you want to enter another? (y to continue): ")
    
    #close the file and output a message
    contact_file.close()
    print("All data saved to coffee.txt.")
#-------------------------------------------------------------------------------------------------------
def read_contact(): #Option 4
    #read_contact accepts no arguments
    #it loops to read the records in coffee.txt
    #and ouputs the description and pounds of coffee
    
    #validate the file exists, if it does -
    #open coffee.txt and read the first description
    if os.path.exists('contact.txt'):
        contact_file = open('contact.txt', 'r')
    else:
        print('File not found.')
        return
    
    desc = contact_file.readline()
    
    while desc != '':
        desc = desc.rstrip('\n')
        pounds = contact_file.readline().rstrip('\n')
        
        #output
        print(f"Description: {desc}")
        print(f"Pounds: {pounds}")
        
        #read the next description
        desc = contact_file.readline()
    #close the file and output a message
    contact_file.close()
    print("All records read.")
#--------------------------------------------------------------------------------------------------------
main()