import time
import random
import string


def createTestData(total_number_of_entries):

    # Code to write  entries to a CSV file and each entry contains a
    # 5-7 letter first name, 5-7 letter last name, 10-20 letter address and a 10 digit phone number
    with open("D:\PythonCodes\/test_data\self_created_mock_data_{}.csv".format(total_number_of_entries), "w") as test_csv_file:
        for i in range(total_number_of_entries):
            first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,7)))
            last_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,7)))
            address = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10,20)))
            phone = ''.join(random.choice(string.digits) for _ in range(10))

            test_csv_file.write("{},{},{},{},{}\n".format(i,first_name,last_name,address,phone))


if __name__ == "__main__":
    start_time = time.time()

    # Call the function to create test data
    createTestData(100)

    end_time = time.time()
    print("Time taken: ", end_time - start_time)