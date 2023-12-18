import os
import csv
import time
from utils.covertFullnameToAscii import add_ascii_values_of_first_and_last_name

# This function goes through the entire address book file and then add another column that contains the
# the ascii value of the full name (merging first and last name) of the record to sort the file two times
# Once on the basis of phone number and another on the basis of name. This file then separate both the 
# sorted files into smaller chunks, each of size n.

# This file then returns two dictionary each containing the file name and first element of each smaller 
# chunk file as ke-pair values, so the we only have to search one file.

def data_pre_processing(file_name, number_of_records_in_each_file=1000):

    # Checking the time it takes to pre-process the entire file and divide it in smaller chunks
    data_pre_processing_started = time.time()

    # Creating a dictionaries that will contain the full name of first element of each file and 
    # phone numbers of the first element of each file along with the file name as key value pairs
    full_names_of_first_element = {}
    phone_numbers_of_first_element = {}

    # Initializing the file name for the file we want to store along with the new ascii column
    file_name_of_file_with_full_name = file_name.replace('.csv', '_with_full_name.csv')

    # Reading the CSV file and creating a new file with the ascii values of the full name
    with open(file_name, "r") as original_contact_records_file:
        with open(file_name_of_file_with_full_name, "w") as contact_records_file_with_full_name:
            
            # Creating a writer and reader object
            writer = csv.writer(contact_records_file_with_full_name, lineterminator='\n')
            reader = csv.reader(original_contact_records_file)

            # Adding the ascii values of the first and last name to the records
            for row in reader:
                row.append(add_ascii_values_of_first_and_last_name(row[1], row[2]))
                writer.writerow(row)
    
    # Creating a folder to store the sorted names if it doesn't exist
    if not os.path.exists(".\/full_names_csv"):
        os.mkdir(".\/full_names_csv")
    
    # Creating a folder to store the sorted phone numbers if it doesn't exist
    if not os.path.exists(".\/phone_numbers_csv"):
        os.mkdir(".\/phone_numbers_csv")

    # Reading the entire file with full name converted into ascii again
    records_with_full_name = []
    with open(file_name_of_file_with_full_name, "r") as contact_records_file_with_ascii:
        records_with_full_name = contact_records_file_with_ascii.readlines()
    
    # Assigning it to another variable for phone numbers
    records_with_full_name.sort(key=lambda x: x.strip().split(",")[4])
    records_sorted_by_phone_numbers = records_with_full_name

    # Sorting the records_with_full_name by full_name
    records_with_full_name.sort(key=lambda x: x.strip().split(",")[5])

    # Writing the sorted records to a new file
    with open('.\/full_names_csv\sorted_by_full_names.csv', "w") as sorted_by_full_name_contact_records_file:
        sorted_by_full_name_contact_records_file.writelines(records_with_full_name)

    # Writing the sorted records to a new file
    with open('.\/full_names_csv\sorted_by_phone_numbers.csv', "w") as sorted_by_phone_numbers_contact_records_file:
        sorted_by_phone_numbers_contact_records_file.writelines(records_sorted_by_phone_numbers)
    
    # Calculating the number of files to be created
    number_of_files = len(records_with_full_name) // number_of_records_in_each_file
    if len(records_with_full_name) % number_of_records_in_each_file != 0:
        number_of_files += 1
    
    # Creating multiple files with number_of_records_in_each_file records each
    for i in range(number_of_files):
        file_name_for_full_names = ".\/full_names_csv\sorted_by_full_names_{}.csv".format(i+1)
        full_names_of_first_element = { file_name_for_full_names: records_with_full_name[i*number_of_records_in_each_file].strip().split(",")[5] } | full_names_of_first_element

        file_name_for_phone_numbers = ".\/phone_numbers_csv\sorted_by_phone_numbers_{}.csv".format(i+1)
        phone_numbers_of_first_element = { file_name_for_phone_numbers: records_sorted_by_phone_numbers[i*number_of_records_in_each_file].strip().split(",")[4] } | phone_numbers_of_first_element

        with open(file_name_for_full_names, "w") as sorted_by_name_file:
            sorted_by_name_file.writelines(records_with_full_name[i*number_of_records_in_each_file:(i+1)*number_of_records_in_each_file])
        
        with open(file_name_for_phone_numbers, "w") as sorted_by_phone_number:
            sorted_by_phone_number.writelines(records_sorted_by_phone_numbers[i*number_of_records_in_each_file:(i+1)*number_of_records_in_each_file])
    
    # store the sorted full names in a file called index.txt
    with open(".\/full_names_csv\index.txt", "w") as index_file:
        index_file.write(str(full_names_of_first_element))
    
    # store the sorted full names in a file called index.txt
    with open(".\/phone_numbers_csv\index.txt", "w") as index_file:
        index_file.write(str(phone_numbers_of_first_element))
        
    # Checking the time taken to pre-process the entire data
    data_pre_processing_ended = time.time()

    # Printing the time taken to pre-process the entire data
    print("Time taken to pre-process the entire data: ", data_pre_processing_ended - data_pre_processing_started)

    # Returning the index files
    return number_of_files, phone_numbers_of_first_element, full_names_of_first_element