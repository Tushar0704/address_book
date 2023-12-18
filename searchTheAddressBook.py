import time
from utils.binarySearch import binary_search

# This function goes through the index file of either phone_numbers or name based
# on the value it is being searched upon.

def search_the_address_book(phone_numbers_of_first_element, full_names_of_first_element, search_text, search_by="phone_numbers"):

    # Checking the time it takes to search the contact in the pre-processed data
    search_started = time.time()

    # If the search by is phone_numbers then look in the phone_numbers_of_first_element file
    # otherwise, look in the full_names_of_first_element file for the record.

    key = 4
    index_file_to_search_in = phone_numbers_of_first_element
    if search_by == "full_names":
        key = 5
        index_file_to_search_in = full_names_of_first_element

    # Now out all the smaller chunks, checking which smaller chunk contains our record
    for file_name_record_is_present in index_file_to_search_in:
        if index_file_to_search_in[file_name_record_is_present] < search_text:
            break
        
    # Getting the content of the file names
    with open(file_name_record_is_present, "r") as file_in_which_records_are:
        sorted_records = file_in_which_records_are.readlines()
    
    # Doing a binary search on the sorted phone numbers/names
    record = binary_search(sorted_records, 0, len(sorted_records) - 1, search_text, key)

    # Printing the record if found
    if record != -1:
        print("Found the record: ", record)
    else:
        print("Record not found") 

    # Checking the time it took to search the contact in the pre-processed data
    search_ended = time.time()

    # Printing the time it took
    print("Time it took to complete the search: ", search_ended - search_started)

    # Returning the record.
    return record