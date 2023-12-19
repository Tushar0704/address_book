from dataPreProcessing import data_pre_processing
from searchTheAddressBook import search_the_address_book
from utils.covertFullnameToAscii import add_ascii_values_of_first_and_last_name

def run():

    file_path = None
    full_names_of_first_element = None
    phone_numbers_of_first_element = None

    # Printing about the address book
    print('This address book takes path to a csv file that contains the records with first name, last name, address and phone number and searches a record in it. - By Tushar Agarwal')

    # Running the code till the user does condition false
    while True:
        print('Please enter: \n1. To input the file path or enter \n2. To search the record based on name \n3. To search the record based on phone number \n0. To Exit')

        user_input = input('Type a number: ')
        if user_input == '1':
            file_path = input('Give the file path to the csv containing the records: ')

            # Pre-Process the file
            phone_numbers_of_first_element, full_names_of_first_element = data_pre_processing(file_path, 1000)
        
        elif user_input == '2' and file_path != None and full_names_of_first_element != None and phone_numbers_of_first_element != None:
            first_name = input('Enter the first name of the user: ')
            last_name = input('Enter the last name of the user: ')

            # Getting the ascii value of the first_name and the last_name of the search
            ascii_value_to_search = add_ascii_values_of_first_and_last_name(first_name, last_name)

            # Searching if it exists or not
            record = search_the_address_book(phone_numbers_of_first_element, full_names_of_first_element, ascii_value_to_search, search_by="full_names")
        
        elif user_input == '2' and (file_path == None or full_names_of_first_element == None or phone_numbers_of_first_element == None):
            print('Please add a record in the address book first')

        elif user_input == '3' and file_path != None and full_names_of_first_element != None and phone_numbers_of_first_element != None:
            phone_number = input('Enter the phone_number of the user: ')

            # Searching if it exists or not
            record = search_the_address_book(phone_numbers_of_first_element, full_names_of_first_element, phone_number, search_by="phone_numbers")
        
        elif user_input == '3' and (file_path == None or full_names_of_first_element == None or phone_numbers_of_first_element == None):
            print('Please add a record in the address book first')  
        
        elif user_input == '0':
            print('Thank you for using the address book. - Tushar Agarwal')
            exit()

        else:
            print('Please choose a correct input!')

if __name__ == "__main__":
    run()