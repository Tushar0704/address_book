import os
import csv
import time
import pandas as pd 

from dataPreProcessing import data_pre_processing
from searchTheAddressBook import search_the_address_book
from utils.covertFullnameToAscii import add_ascii_values_of_first_and_last_name


# This function does a binary search on a given sorted list
def binary_search(arr, low, high, x, key=4):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid].strip().split(',')[key] == x:
            return arr[mid]
 
        # If element is smaller than mid, then it can only
        # be present in left sub array
        elif arr[mid].strip().split(',')[key] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x) 
    else:
        # Element is not present in the array
        return -1


def add_ascii_values_of_first_and_last_name(first_name, last_name):
    # Initializing the ascii value of the first name
    name_ascii_value = ''

    # Creating a full name by combining the first and last name
    name = first_name.upper() + last_name.upper()   
    
    # Calculating the ascii value of the full name
    for character in name:
        name_ascii_value += str(ord(character))
    
    return name_ascii_value




# This function goes through the input csv file and creates a folder
# that contains multiple csv files with 1000000 records each and each file is sorted based on name
# It returns the number of files created along with a dictionary that contains the first name of each file
# along with the file name as key value pairs
def sort_csv_based_on_names_and_create_multiple_csv_files(file_name, number_of_records_in_each_file=1000):

    # Checking the time taken to sort the CSV file and create multiple files
    sort_csv_based_on_names_and_create_multiple_files_started = time.time()

    # Creating a dictionary that will contain the first full name of each file along with the file name as key value pairs
    first_full_names = {}

    # Initializing the file name to store the ascii values of the full name
    file_name_with_ascii_value = file_name.replace('.csv', '_full_name.csv')

    # Reading the CSV file and creating a new file with the ascii values of the full name
    # with open(file_name, "r") as original_contact_records_file:
    #     with open(file_name_with_ascii_value, "w") as sorted_contact_records_file:
            
    #         # Creating a writer and reader object
    #         writer = csv.writer(sorted_contact_records_file, lineterminator='\n')
    #         reader = csv.reader(original_contact_records_file)

    #         # Sorting the records based on full name
    #         sorted_by_name = []

    #         # Adding the ascii values of the first and last name to the records
    #         for row in reader:
    #             row.append(add_ascii_values_of_first_and_last_name(row[1], row[2]))
    #             sorted_by_name.append(row)

    #         # Writing the records with full name to a new file
    #         writer.writerows(sorted_by_name)
    

    sorted_by_name=[]

    # Read the new file with the ascii values of the full name and sort it
    with open(file_name_with_ascii_value, "r") as contact_records_file_with_ascii:
        sorted_by_name = contact_records_file_with_ascii.readlines()

    # Sorting the records based on full name
    sorted_by_name.sort(key=lambda x: x.strip().split(",")[5])

    # Writing the sorted records to a new file
    with open(file_name_with_ascii_value.replace('.csv', '_sorted.csv'), "w") as sorted_contact_records_file:
        sorted_contact_records_file.writelines(sorted_by_name)

    # Calculating the number of files to be created
    number_of_files = len(sorted_by_name) // number_of_records_in_each_file
    if len(sorted_by_name) % number_of_records_in_each_file != 0:
        number_of_files += 1

    # Creating a folder to store the sorted names if it doesn't exist
    if not os.path.exists(".\/names_csv"):
        os.mkdir(".\/names_csv")

    # Creating multiple files with number_of_records_in_each_file records each
    for i in range(number_of_files):
        file_name = ".\/names_csv\sorted_by_names_{}.csv".format(i+1)
        first_full_names = { file_name: sorted_by_name[i*number_of_records_in_each_file].strip().split(",")[5] } | first_full_names
        with open(file_name, "w") as sorted_names_file:
            sorted_names_file.writelines(sorted_by_name[i*number_of_records_in_each_file:(i+1)*number_of_records_in_each_file])
    
    # Checking the time taken to sort the CSV file and create multiple files
    sort_csv_based_on_names_and_create_multiple_files_ended = time.time()

    # store the sorted full names in a file called index.txt
    with open(".\/names_csv\index.txt", "w") as index_file:
        index_file.write(str(first_full_names))

    # Printing the time taken to sort the CSV file and create multiple files
    print("Time taken to sort and create multiple files: ", sort_csv_based_on_names_and_create_multiple_files_ended - sort_csv_based_on_names_and_create_multiple_files_started)

    # Returning the number of files created along with a dictionary that contains the first full name of each file along with the file name as key value pairs
    return number_of_files, first_full_names, number_of_records_in_each_file


# This function goes through the input csv file and creates a folder
# that contains multiple csv files with 1000000 records each and each file is sorted based on phone numbers
# It returns the number of files created along with a dictionary that contains the first phone number of each file
# along with the file name as key value pairs
def sort_csv_based_on_phone_and_create_multiple_csv_files(file_name, number_of_records_in_each_file=1000):
    # Checking the time taken to sort the CSV file and create multiple files
    sort_csv_based_on_phone_and_create_multiple_files_started = time.time()

    # Creating a dictionary that will contain the first phone number of each file along with the file name as key value pairs
    first_phone_numbers = {}

    # Reading the CSV file
    with open(file_name, "r") as original_contact_records_file:
        contact_records = original_contact_records_file.readlines()

    # Sorting the records based on phone number
    contact_records.sort(key=lambda x: x.strip().split(",")[4])

    # Writing the sorted records to a new file
    with open(file_name.replace('.csv', '_sorted.csv'), "w") as sorted_contact_records_file:
        sorted_contact_records_file.writelines(contact_records)
    
    # Calculating the number of files to be created
    number_of_files = len(contact_records) // number_of_records_in_each_file
    if len(contact_records) % number_of_records_in_each_file != 0:
        number_of_files += 1

    # Creating a folder to store the sorted phone numbers if it doesn't exist
    if not os.path.exists(".\phone_numbers_csv"):
        os.mkdir(".\phone_numbers_csv")

    # Creating multiple files with number_of_records_in_each_file records each
    for i in range(number_of_files):
        file_name = ".\phone_numbers_csv\sorted_by_phone_numbers_{}.csv".format(i+1)
        first_phone_numbers = { file_name: contact_records[i*number_of_records_in_each_file].strip().split(",")[4] } | first_phone_numbers
        with open(file_name, "w") as sorted_phone_numbers_file:
            sorted_phone_numbers_file.writelines(contact_records[i*number_of_records_in_each_file:(i+1)*number_of_records_in_each_file])
    
    # Checking the time taken to sort the CSV file and create multiple files
    sort_csv_based_on_phone_and_create_multiple_files_ended = time.time()

    # store the sorted phone numbers in a file called index.txt
    with open(".\phone_numbers_csv\index.txt", "w") as index_file:
        index_file.write(str(first_phone_numbers))

    # Printing the time taken to sort the CSV file and create multiple files
    print("Time taken to sort and create multiple files: ", sort_csv_based_on_phone_and_create_multiple_files_ended - sort_csv_based_on_phone_and_create_multiple_files_started)

    # Returning the number of files created along with a dictionary that contains the first phone number of each file along with the file name as key value pairs
    return number_of_files, first_phone_numbers, number_of_records_in_each_file


# This function goes through the input csv file and creates a folder
# that contains multiple csv files with 1000000 records each and each file is sorted based on phone numbers
# It returns the number of files created along with a dictionary that contains the first phone number of each file
# along with the file name as key value pairs
def sort_csv_based_on_phone_and_create_multiple_txt_files(file_name, number_of_records_in_each_file=1000):

    # Creating a dictionary that will contain the first phone number of each file along with the file name as key value pairs
    first_phone_numbers = {}

    # Reading the CSV file
    with open(file_name, "r") as original_contact_records_file:
        contact_records = original_contact_records_file.readlines()

    # Sorting the records based on phone number
    contact_records.sort(key=lambda x: x.strip().split(",")[4])

    # Writing the sorted records to a new file
    with open(file_name.replace('.csv', '_sorted.csv'), "w") as sorted_contact_records_file:
        sorted_contact_records_file.writelines(contact_records)
    
    # Creating an array of sorted phone numbers
    sorted_phone_numbers = []
    for contact_record in contact_records:
        sorted_phone_numbers.append(contact_record.strip().split(",")[4])
    
    # Calculating the number of files to be created
    number_of_files = len(sorted_phone_numbers) // number_of_records_in_each_file
    if len(sorted_phone_numbers) % number_of_records_in_each_file != 0:
        number_of_files += 1

    # Creating a folder to store the sorted phone numbers if it doesn't exist
    if not os.path.exists(".\phone_numbers"):
        os.mkdir(".\phone_numbers")
    
    # Creating multiple files with number_of_records_in_each_file records each
    for i in range(number_of_files):
        file_name = ".\phone_numbers\sorted_phone_numbers_{}.txt".format(i+1)
        first_phone_numbers = { file_name: sorted_phone_numbers[i*number_of_records_in_each_file] } | first_phone_numbers
        # first_phone_numbers[file_name] = sorted_phone_numbers[i*number_of_records_in_each_file]
        with open(file_name, "w") as sorted_phone_numbers_file:
            sorted_phone_numbers_file.writelines('\n'.join(sorted_phone_numbers[i*number_of_records_in_each_file:(i+1)*number_of_records_in_each_file]))
    
    # store the sorted phone numbers in a file called index.txt
    with open(".\phone_numbers\index.txt", "w") as index_file:
        index_file.write(str(first_phone_numbers))

    # Printing that the files have been created
    print("The file has been sorted and multiple files have been created")

    # Returning the number of files created along with a dictionary that contains the first phone number of each file along with the file name as key value pairs
    return number_of_files, first_phone_numbers, number_of_records_in_each_file


# This function goes through the entire CSV file and will sort it based on phone numbers
def sort_csv_based_on_phone():

    # Checking the time taken to sort the CSV file
    sort_started = time.time()

    with open(".\/test_data\self_created_mock_data_10000000.csv", "r") as test_csv_file:
        contact_records = test_csv_file.readlines()
    
    # Sorting the records based on phone number
    contact_records.sort(key=lambda x: x.strip().split(",")[4])
    
    # Writing the sorted records to a new file
    with open(".\/test_data\self_created_mock_data_10000000.csv", "w") as sorted_csv_file:
        sorted_csv_file.writelines(contact_records)
    
    # Creating an array of sorted phone numbers
    sorted_phone_numbers = []
    for contact_record in contact_records:
        sorted_phone_numbers.append(contact_record.strip().split(",")[4])
    
    # Store the sorted phone numbers in a file
    with open("sorted_phone_numbers_10000000.txt", "w") as sorted_phone_numbers_file:
        sorted_phone_numbers_file.writelines('\n'.join(sorted_phone_numbers))
    
    # Calculating the time taken to sort the CSV file
    sort_ended = time.time()
    print("Time taken to sort: ", sort_ended - sort_started)


# This function goes through the entire CSV file and checks if the phone number is 81410121814
# This takes approximately 0.00099 seconds to run for 1000 records
def simple_read():
    with open("mock_data_1000.csv", "r") as test_csv_file:
        for contact_record in test_csv_file:
            
            # Getting the values from the CSV file
            id,first_name,last_name,address,phone = contact_record.strip().split(",")
            
            # Checking if the phone number is 81410121814
            if phone == "81410121814":
                print("Found the record: ", contact_record)
                break


# This function goes through the entire CSV file and checks if the phone number is 81410121814
# But the data only consists of name and phone number and we only need the phone number - Takes same time as simple_read
def simple_read_with_name_and_phone():
    with open("mock_data_just_phone_and_name.csv", "r") as test_csv_file:
        for contact_record in test_csv_file:
            
            # Getting the values from the CSV file
            id,name,phone = contact_record.strip().split(",")
            
            # Checking if the phone number is 81410121814
            if phone == "81410121814":
                print("Found the record: ", contact_record)
                break


# This function does a binary search on the sorted phone numbers list
def simple_binary_search_on_sorted_list_csv(number_of_files, index_file, number_of_records_in_each_file, search_text, search_by="phone"):

    # Checking which file the phone number/name is in
    for file_name in index_file:
        if index_file[file_name] < search_text:
            break
    
    # Getting the sorted file
    with open(file_name, "r") as sorted_file:
        sorted_records = sorted_file.readlines()

    # Getting the index of the number/name
    key = 4
    if search_by == "name":
        key = 5
       
    # Doing a binary search on the sorted phone numbers/names
    record = binary_search(sorted_records, 0, len(sorted_records) - 1, search_text, key)

    # Printing the record if found
    if record != -1:
        print("Found the record: ", record)
    else:
        print("Record not found") 

    return record


# This function does a binary search on the sorted phone numbers list
def simple_binary_search_on_sorted_phone_numbers_txt(number_of_files, first_phone_numbers, number_of_records_in_each_file, number_to_search):

    # Checking the time taken to read the sorted phone numbers
    simple_binary_search_on_sorted_phone_numbers_started = time.time()

    # Checking which file the phone number is in
    for file_name in first_phone_numbers:
        if first_phone_numbers[file_name] < number_to_search:
            break
    
    # Getting the index of the file
    file_index = int(file_name.split("_")[-1].split(".")[0]) - 1

    # Getting the sorted file
    with open(file_name, "r") as sorted_phone_numbers_file:
        sorted_phone_numbers = [phone_number.rstrip('\n') for phone_number in sorted_phone_numbers_file.readlines()]
       
    # Doing a binary search on the sorted phone numbers
    index = binary_search(sorted_phone_numbers, 0, len(sorted_phone_numbers) - 1, number_to_search)
    correct_index = index + (file_index * number_of_records_in_each_file)

    # Checking the time taken to do a binary search on the sorted phone numbers
    simple_binary_search_on_sorted_phone_numbers_ended = time.time()
    
    # Getting the record from the CSV file
    with open(".\/test_data\self_created_mock_data_10000000_sorted.csv", "r") as test_csv_file:
        contact_records = test_csv_file.readlines()
    
    # Getting the record
    record = contact_records[correct_index].strip().split(",")

    # df = pd.read_csv('.\/test_data\self_created_mock_data_10000000_sorted.csv')
    # record = df.loc[[correct_index],:]

    file_ended = time.time()

    print("index: ", index)
    print("correct_index: ", correct_index)

    # Printing the record
    print("Time taken to find the record: ", file_ended - simple_binary_search_on_sorted_phone_numbers_ended)
    print("Found the record: ", record) 

    # Printing the total time taken to read the sorted phone numbers and do a binary search
    print("Total time taken: ", simple_binary_search_on_sorted_phone_numbers_ended - simple_binary_search_on_sorted_phone_numbers_started)


def run():
    # simple_read()
    # simple_read_with_name_and_phone()
    # sort_csv_based_on_phone()

    # number_of_files, first_phone_numbers, number_of_records_in_each_file = sort_csv_based_on_phone_and_create_multiple_csv_files(".\/test_data\self_created_mock_data_10000000.csv")
    # simple_binary_search_on_sorted_phone_numbers_csv(number_of_files, first_phone_numbers, number_of_records_in_each_file, number_to_search="9992066309")

    number_of_files, phone_numbers_of_first_element, full_names_of_first_element = data_pre_processing("D:\PythonCodes\/test_data\self_created_mock_data_100.csv", 1000)

    ascii_value_to_search = add_ascii_values_of_first_and_last_name("zipvpy", "dzeewrm")
    print(ascii_value_to_search)

    record = search_the_address_book(phone_numbers_of_first_element, full_names_of_first_element, ascii_value_to_search, search_by="full_names")

    # number_of_files, first_phone_numbers, number_of_records_in_each_file = sort_csv_based_on_phone_and_create_multiple_txt_files(".\/test_data\self_created_mock_data_10000000.csv")
    # simple_binary_search_on_sorted_phone_numbers_txt(number_of_files, first_phone_numbers, number_of_records_in_each_file, number_to_search="8141012184")


if __name__ == "__main__":
    start_time = time.time()
    
    run()
    
    end_time = time.time()
    print("Total time taken: ", end_time - start_time)