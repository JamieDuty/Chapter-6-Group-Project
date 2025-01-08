#Contact Manager
import os

#contact manager menu
def contact_manager():
    # Contact manager accepts no arguments
    # It displays and returns a menu choice
    
    while True:
        # Display menu
        print('Choose a contact option:')
        print('1) Add a record')
        print('2) Modify a record')
        print('3) Delete a record')
        print('4) Display all saved records')
        print('5) Search for a record')
        print('6) Exit')

        # Get the user's choice
        choice = input('Contact Option: ')
        
        # Validate if the input is a number and between 1 and 6
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 6:
                return choice  # Return valid choice
            else:
                print("Invalid choice! Please choose a number between 1 and 6.")
        else:
            print("Invalid input! Please enter a valid number (not a letter or special character).")
#-----------------------------------------------------------------------------------------------------------------
def main(): 
    # Contact manager accepts no arguments
    # It calls contact_manager to display a menu to the user
    # and calls each function according to the user input
    
    # Prime the loop with a valid choice from contact_manager
    choice = contact_manager()
    
    # Loop to call the desired function based on the choice
    while choice != 3:
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

        # Get the next valid choice from the user
        choice = contact_manager()
    
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
def modify_contact():  # Option 2
    # modify_contact accepts no arguments
    # It uses the os module to perform file-related operations

    # Boolean variable to check if the contact was found
    found = False

    # Get the contact description to search for and new details for modification
    search = input('Enter the contact name to modify: ')
    new_name = input('Enter the new name: ')
    new_address = input('Enter the new address: ')
    new_phone = input('Enter the new phone number: ')
    new_email = input('Enter the new email: ')

    # Open the contact.txt to read and a new temporary file to write
    with open('contact.txt', 'r') as contact_file, open('newnumber.txt', 'w') as temp_file:
        # Read the first record to prime the loop
        name = contact_file.readline()

        while name != '':
            # Read the next lines: address, phone, and email
            address = contact_file.readline().rstrip('\n')
            phone = contact_file.readline().rstrip('\n')
            email = contact_file.readline().rstrip('\n')

            # Strip newline characters from name
            name = name.rstrip('\n')

            # Search for the contact to modify
            if search.lower() == name.lower():  # If contact has been found
                temp_file.write(new_name + '\n')
                temp_file.write(new_address + '\n')
                temp_file.write(new_phone + '\n')
                temp_file.write(new_email + '\n')
                found = True
            else:
                # Write the current contact's data to the temp file (unchanged)
                temp_file.write(name + '\n')
                temp_file.write(address + '\n')
                temp_file.write(phone + '\n')
                temp_file.write(email + '\n')

            # Read the next name for the next record
            name = contact_file.readline()

    # After processing, delete the original file and rename the temporary file
    if found:
        os.remove('contact.txt')  # Delete the original contact file
        os.rename('newnumber.txt', 'contact.txt')  # Rename the temp file to contact.txt
        print(f"The details for {search} have been updated in the file.")
    else:
        os.remove('newnumber.txt')  # Remove the temporary file if no contact was found
        print("Record not found...")
#-----------------------------------------------------------------------------------------------------
def delete_contact():  # Option 3
    # delete accepts no arguments
    # it opens the file contact.txt and searches for a string to delete
    # it writes every record except for the record to delete
    # to a temporary file and deletes the old file
    # it renames the temp file to contact.txt and closes the files
    
    # Boolean flag variable
    found = False
    
    # Take input from the user for the search criteria
    search = input('Enter contact name to delete: ')
    
    # Open the contact.txt file to read and a new temp file to write
    contact_file = open('contact.txt', 'r')
    temp_file = open('newnumber.txt', 'w')
    
    # Read the first name to prime the loop
    name = contact_file.readline()
    
    while name != '':
        # Read the next lines: address, phone, and email
        address = contact_file.readline().rstrip('\n')
        phone = contact_file.readline().rstrip('\n')
        email = contact_file.readline().rstrip('\n')
        
        # Strip newline from name
        name = name.rstrip('\n')

        # Search for and delete the record
        if search.lower() != name.lower():  # If this is a record we need to keep
            # Write all fields to the temp file
            temp_file.write(name + '\n')
            temp_file.write(address + '\n')
            temp_file.write(phone + '\n')
            temp_file.write(email + '\n')
 
            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(number + '\n')
            
        #read the next description
        name = contact_file.readline()
        
    #close the files    
    contact_file.close()
    temp_file.close()
    
    #all files have been processed and closed. Delete and rename the files
    #delete the orignal
    os.remove('contact.txt')
    #rename the temp file to coffee.txt
    os.rename('newnumber.txt', 'contact.txt')
    
    #notify user the coffee was not found in the file
    if not found:
        print ('\nRecord not found...')
    else:
        print ('The details for', search, 'has been updated to the file.')
#-----------------------------------------------------------------------------------------------------
def delete_contact():   #Option 3
    #delete accepts no arguments
    #it opens the file contact.txt and searches for a string to delete
    # it writes every record except for the record to delete
    #to a tempoary file and deletes the old file
    #it renames temp to coffee and closes the file
    
    #boolean flag variable
    found = False
    
    #Take input from the user for the search criteria
    search = input('Enter contact to delete: ')
    
    #open the contact.txt file to read and a new temp file to write
    contact_file = open('contact.txt', 'r')
    temp_file = open('newnumber.txt', 'w')
    
    #read the first description
    name = contact_file.readline()
    
    #loop the read nad process each record
    while name != '':
        number = contact_file.readline()
        street = contact_file.readline()
        email = contact_file.readline()
        
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
            temp_file.write(address + '\n')
            temp_file.write(address + '\n')

        else:
            found = True

        # Read the next name for the next record
        name = contact_file.readline()

    # All records have been processed, now check if found and handle files
    contact_file.close()
    temp_file.close()

    if found:
        # Delete the original file
        os.remove('contact.txt')  
        # Rename the temp file to contact.txt
        os.rename('newnumber.txt', 'contact.txt')
        print(f'{search} has been deleted from contact.txt.')
    else:
        # If the contact was not found, delete the temporary file
        os.remove('newnumber.txt')  
        print('\nRecord not found.\n')
#--------------------------------------------------------------------------------------------------
def read_contact():  # Option 4
    # read_contact accepts no arguments
    # It loops to read the records in contact.txt
    # and outputs the name, address, phone, and email

    # Validate if the file exists
    if os.path.exists('contact.txt'):
        contact_file = open('contact.txt', 'r')
    else:
        print('File not found.')
        return

    # Read the first record
    name = contact_file.readline()
    
    # Loop through each record in the file
    while name != '':
        name = name.rstrip('\n')
        address = contact_file.readline().rstrip('\n')
        phone = contact_file.readline().rstrip('\n')
        email = contact_file.readline().rstrip('\n')
        
        # Output the contact information
        print()
        print(f"Name: {name}")
        print(f"Address: {address}")
        print(f"Phone Number: {phone}")
        print(f"Email: {email}")
        print()  # Add a blank line for better readability between records

        # Read the next name (start of next record)
        name = contact_file.readline()

    # Close the file and output a message
    contact_file.close()
    print("All records read.")
#-----------------------------------------------------------------------------------------------------
def search_contact():  # Option 5
    # search_contact accepts no arguments
    # It searches contact.txt for a string the user enters
    # If no record matches, it outputs a message to the user

    # Initialize a boolean flag variable
    found = False

    # Get input from the user
    search = input("Enter the contact name to search for: ")

    # Open contact.txt to read
    contact_file = open("contact.txt", 'r')

    # Get the first description to prime the loop
    name = contact_file.readline()

    while name != '':
        # Read the next lines: address, phone, and email
        address = contact_file.readline().rstrip('\n')
        phone = contact_file.readline().rstrip('\n')
        email = contact_file.readline().rstrip('\n')

        # Strip newline from name
        name = name.rstrip('\n')

        # Check if the name matches the search string
        if name.lower() == search.lower():
            print("\n---Record found!---")
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Phone Number: {phone}")
            print(f"Email: {email}")
            # Item found, toggle boolean to true
            found = True
            break

        # Get another name (next record)
        name = contact_file.readline()

    # Close the file
    contact_file.close()

    if not found:
        print("Record not found")
#--------------------------------------------------------------------------------------------------------
main()