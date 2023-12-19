import os
import csv
import heapq
from itertools import islice

def merge_sorted_files(temporary_files, output_file, key):
        with open(output_file, 'w', newline='') as out:
            csv_file_writer = csv.writer(out)
            heap = []

            # Initialize the heap with the first row from each file
            for f in temporary_files:
                reader = csv.reader(f)
                row = next(reader, None)
                if row is not None:
                    heapq.heappush(heap, (int(row[key]), row, reader))

            # Merge chunks
            while heap:
                value, row, reader = heapq.heappop(heap)
                csv_file_writer.writerow(row)
                next_row = next(reader, None)
                if next_row is not None:
                    heapq.heappush(heap, (int(next_row[key]), next_row, reader))


def merge_sort_csv(input_file, output_file, chunk_size, key = 4):
    # Step 1: Split the CSV file into sorted chunks
    temp_files = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        i = 0
        while True:
            chunk = list(csv.reader(islice(f, chunk_size)))
            if not chunk:
                break
            chunk.sort(key=lambda x: int(x[key]))  # Sort each chunk using built-in Python sort
            temp_file = f'temp_chunk_{i}.csv'
            with open(temp_file, 'w', newline='') as temp:
                writer = csv.writer(temp)
                writer.writerows(chunk)
            temp_files.append(open(temp_file, 'r'))
            i += 1
    
    # Step 2: Merge sorted chunks
    merge_sorted_files(temp_files, output_file, key)

    # Cleanup: Close and remove temporary files
    for f in temp_files:
        f.close()
        os.remove(f.name)