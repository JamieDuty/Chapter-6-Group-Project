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
    contact_file = open('contact.txt', 'a')
    
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
    print("All data saved to contact.txt.")
#-------------------------------------------------------------------------------------------------------
def modify_contact(): #Option 2
    #modify contact accepts no arguments
    #it imports the os module - this is needed to perform OS related file commands
    #it searches through the records and allows the user to modify the record
    
    #boolean flag variable
    found = False
    
    #get inputs from the user
    search = input("Enter the coffee description to modify: ")
    newQty = input("Enter the new quantity (in pounds): ")
    
    #open coffee.txt to read and a new temporary file to write
    coffee_file = open("coffee.txt", 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first description to prime the loop
    desc = coffee_file.readline()
    
    #loop to read and process each record
    while desc != '':
        qty = coffee_file.readline()
        
        #strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower(): #coffee found, add it AND new qty to temp file
            #write the description to temp.txt
            temp_file.write(desc + '\n')
            temp_file.write(newQty + '\n')
            found = True
            break
        else: #not the coffee you are looking for, write original description and original quantity to temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
            
        #read the next description
        desc = coffee_file.readline()
        
    #close both files
    coffee_file.close()
    temp_file.close()
    
    #delete the original coffee.txt
    os.remove('coffee.txt')
    
    #rename temp.txt to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
    
    #description not found
    if not found:
        print('\nRecord not found!')
    else:
        print(f"The quantity for {desc} has been changed from {qty} to {newQty}.")
#----------------------------------------------------------------------------------------------------------
def delete_contact(): #Option 3
    #delete accepts no arguments
    #it opens the file coffee.txt and searches for a string to delete
    # it writes every record except for the record to delete
    #to a tempoary file and deletes the old file
    #it renames temp to coffee and closes the file
    
    #boolean flag variable
    found = False
    
    #Take input from the user for the search criteria
    search = input('Enter contact to delete: ')
    
    #open the coffee.txt file to read and a new temp file to write
    contact_file = open('contact.txt', 'r')
    temp_file = open('newnumber.txt', 'w')
    
    #read the first description
    name = contact_file.readline()
    
    #loop the read nad process each record
    while name != '':
        number = contact_file.readline()
        
        #strip newline
        name = name.rstrip('\n')
        address = name.rstrip('\n')
        number = name.rstrip('\n')
        email = name.rstrip('\n')
        
        #search for and delete the record
        if search.lower() != name.lower(): #this is a record we need to keep
            #write both to the temp file
            temp_file.write(number + '\n')
            temp_file.write(name + '\n')
        else:
            found = True
            
        #read the next description
        name = contact_file.readline()
            
    #all record have been processed, close, remove, and rename files
    contact_file.close()
    temp_file.close()
    
    os.remove('contact.txt') # elete the orginal
    os.rename('newnumber.txt', 'contact.txt') #rename temp to coffee
    
    #confirm deletion to the user
    if not found: #this is the same as if found == False
        print ( '\nRecord not found.\n')
    else:
        print (search, 'has been deleted from contact.txt')
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
    
    name = contact_file.readline()

    while name != '':
        name = name.rstrip('\n')
        address = contact_file.readline().rstrip('\n')
        phone = contact_file.readline().rstrip('\n')
        email = contact_file.readline().rstrip('\n')
       
        #output
        print(f"Name: {name}")
        print(f"Address: {address}")
        print(f"Phone Number: {phone}")
        print(f"Email: {email}")
    
        #read the next description
        name = contact_file.readline()
    #close the file and output a message
    contact_file.close()
    print("All records read.")
#--------------------------------------------------------------------------------------------------------
def search_contact(): #Option 5
    #search contact accepts no arguments
    #it searches contact.txt for a string the user enters
    #if no record matches, it outputs a message to the user
    
    #initialize a boolean flag variable
    found = False
    
    #get input from the user
    search = input("Enter the contact name to search for: ")
    
    #open contact.txt to read
    contact_file = open("contact.txt", 'r')
    
    #get the first description to prime the loop
    name = contact_file.readline()
    
    while name != '':
        # read the next line, address
        address = contact_file.readline()
        phone = contact_file.readline()
        email = contact_file.readline()
        
        #strip newline from name
        name = name.rstrip('\n')
        
        #check if the desc == search string
        if name.lower() == search.lower():
            print("\n---Record found!---")
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Phone Number: {phone}")
            print(f"Email: {email}")
            #Item found, toggle boolean to true
            found = True
            break
        
        #get another description
        name = contact_file.readline()
    
    #close the file
    contact_file.close()
    
    if not found:
        print("Record not found")
#----------------------------------------------------------------------------------------------------------

main()