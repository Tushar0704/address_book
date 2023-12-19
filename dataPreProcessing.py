import os
import csv
import time

from utils.mergeSortCSV import merge_sort_csv
from utils.splitFileIntoChunks import split_file_into_chunks
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

    # Initializing the total number of records in the file
    total_number_of_Records = 0

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
                total_number_of_Records += 1
                row.append(add_ascii_values_of_first_and_last_name(row[1], row[2]))
                writer.writerow(row)
    
    # Creating a folder to store the sorted names if it doesn't exist
    if not os.path.exists(".\/full_names_csv"):
        os.mkdir(".\/full_names_csv")
    
    # Creating a folder to store the sorted phone numbers if it doesn't exist
    if not os.path.exists(".\/phone_numbers_csv"):
        os.mkdir(".\/phone_numbers_csv")

    # Sorting the file with full name based on full name and on based of phone_numbers
    merge_sort_csv(file_name_of_file_with_full_name, '.\/full_names_csv\sorted_by_full_names.csv', number_of_records_in_each_file, 5)
    merge_sort_csv(file_name_of_file_with_full_name, '.\/phone_numbers_csv\sorted_by_phone_numbers.csv', number_of_records_in_each_file, 4)
    
    # Calculating the number of files to be created
    number_of_files = total_number_of_Records // number_of_records_in_each_file
    if total_number_of_Records % number_of_records_in_each_file != 0:
        number_of_files += 1

    # Splitting the sorted_by_full_names csv file into smaller chunks
    full_names_of_first_element = split_file_into_chunks('.\/full_names_csv\sorted_by_full_names.csv', '.\/full_names_csv\sorted_by_full_names_', number_of_records_in_each_file, 5)

    # Splitting the sorted_by_phone_numbers csv file into smaller chunks
    phone_numbers_of_first_element = split_file_into_chunks('.\/phone_numbers_csv\sorted_by_phone_numbers.csv', '.\/phone_numbers_csv\sorted_by_phone_numbers_', number_of_records_in_each_file, 4)

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