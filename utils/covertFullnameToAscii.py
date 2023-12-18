# This function takes first_name and last_name of the record as input
# and combine them and then convert into the ascii value of it.

def add_ascii_values_of_first_and_last_name(first_name, last_name):
    # Initializing the ascii value of the first name
    name_ascii_value = ''

    # Creating a full name by combining the first and last name
    name = first_name.upper() + last_name.upper()   
    
    # Calculating the ascii value of the full name
    for character in name:
        name_ascii_value += str(ord(character))
    
    return name_ascii_value