import os
import time


# This function does a binary search on a given sorted list
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x) 
    else:
        # Element is not present in the array
        return -1


# This function goes through the input csv file and creates a folder
# that contains multiple csv files with 1000000 records each and each file is sorted based on phone numbers
# It returns the number of files created along with a dictionary that contains the first phone number of each file
# along with the file name as key value pairs
def sort_csv_based_on_phone_and_create_multiple_files(file_name, number_of_records_in_each_file=1000):
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
    
    # Checking the time taken to sort the CSV file and create multiple files
    sort_csv_based_on_phone_and_create_multiple_files_ended = time.time()

    # store the sorted phone numbers in a file called index.txt
    with open(".\phone_numbers\index.txt", "w") as index_file:
        index_file.write(str(first_phone_numbers))

    # Printing the time taken to sort the CSV file and create multiple files
    print("Time taken to sort and create multiple files: ", sort_csv_based_on_phone_and_create_multiple_files_ended - sort_csv_based_on_phone_and_create_multiple_files_started)

    # Returning the number of files created along with a dictionary that contains the first phone number of each file along with the file name as key value pairs
    return number_of_files, first_phone_numbers, number_of_records_in_each_file


# This function goes through the entire CSV file and will sort it based on phone numbers
def sort_csv_based_on_phone():

    # Checking the time taken to sort the CSV file
    sort_started = time.time()

    with open(".\create_test_data\self_created_mock_data_10000000.csv", "r") as test_csv_file:
        contact_records = test_csv_file.readlines()
    
    # Sorting the records based on phone number
    contact_records.sort(key=lambda x: x.strip().split(",")[4])
    
    # Writing the sorted records to a new file
    with open(".\create_test_data\self_created_mock_data_10000000.csv", "w") as sorted_csv_file:
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
def simple_binary_search_on_sorted_phone_numbers(number_of_files, first_phone_numbers, number_of_records_in_each_file, number_to_search):

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
    index = binary_search(sorted_phone_numbers, 0, len(sorted_phone_numbers) - 1, "8141012184")
    correct_index = index + (file_index * number_of_records_in_each_file)

    # Checking the time taken to do a binary search on the sorted phone numbers
    simple_binary_search_on_sorted_phone_numbers_ended = time.time()
    
    # Getting the record from the CSV file
    with open(".\create_test_data\self_created_mock_data_10000000_sorted.csv", "r") as test_csv_file:
        contact_records = test_csv_file.readlines()
    
    record = contact_records[correct_index].strip().split(",")

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
    number_of_files, first_phone_numbers, number_of_records_in_each_file = sort_csv_based_on_phone_and_create_multiple_files(".\create_test_data\self_created_mock_data_10000000.csv")
    simple_binary_search_on_sorted_phone_numbers(number_of_files, first_phone_numbers, number_of_records_in_each_file, number_to_search="8141012184")


if __name__ == "__main__":
    start_time = time.time()
    
    run()
    
    end_time = time.time()
    print("Total time taken: ", end_time - start_time)