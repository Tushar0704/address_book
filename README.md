# Address Book

A CLI-based address book that can:

  1. Add contacts with :
    a. First Name
    b. Last Name
    c. Address
    d. Phone Number
  2. Search the contact based on :
    a. Name
    b. Phone Number

The address book should be able to store 1 billion+ contacts and return search results under a millisecond.

Your code should be :
1. Executable with mock data
2. Extendible and follow proper design patterns
3. Please do not use databases or in-built functions


## How to Use the Address Book
### Introduction
This address book software allows you to store and search for contacts based on either their names or phone numbers. Here's a step-by-step guide on how to use it.

### Initial Setup
Make sure your CSV file contains records with the following columns:
  1. First Name
  2. Last Name
  3. Address
  4. Phone Number

### Using the Address Book
Starting the Address Book:

Run the script containing the provided code.
You'll see a welcome message and instructions on how to proceed.
Options Available:

Upon starting, you'll be presented with several options:
1. Input the file path: To add a new CSV file.
2. Search based on name: Search for contacts by their names.
3. Search based on phone number: To search for contacts by their phone numbers.
0. Exit: To close the address book.
Inputting a File:

Choose option 1.
Enter the path to your CSV file when prompted.
Wait for approximately 60 seconds (For CSV with 1M rows) as the file is preprocessed.
Once processed, the address book will display a message indicating success.


Choose option 2.
Searching by Name:
Enter the first and last names of the contact you wish to find.
The address book will search for the contact and display the results if found.


Choose option 3.
Searching by Phone Number:
Enter the phone number of the contact you wish to find.
The address book will search for the contact and display the results if found.
Exiting the Address Book:


Choose option 0.
You'll see a goodbye message, and the address book will close.


## Test Data
There is a folder, create_test_data that contains a script to create test data for testing purposes.

<br>
Notes:
For large CSV files, be patient during the preprocessing phase.
Make sure to enter accurate names or phone numbers for searching to get the desired results.
