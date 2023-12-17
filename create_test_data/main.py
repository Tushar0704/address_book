import time
import random
import string


def createTestData():

    # Code to write  entries to a CSV file and each entry contains a
    # 5-7 letter first name, 5-7 letter last name, 10-20 letter address and a 10 digit phone number
    with open("D:\PythonCodes\createTestData\self_created_mock_data_10000000.csv", "w") as test_csv_file:
        for i in range(10000000):
            first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,7)))
            last_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5,7)))
            address = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10,20)))
            phone = ''.join(random.choice(string.digits) for _ in range(10))

            test_csv_file.write("{},{},{},{},{}\n".format(i,first_name,last_name,address,phone))


if __name__ == "__main__":
    start_time = time.time()

    createTestData()

    end_time = time.time()
    print("Time taken: ", end_time - start_time)