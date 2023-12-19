# This file takes the csv and divides into multiple small CSVs
def split_file_into_chunks(main_file, chunks_file_name, chunk_size = 1000, key = 4):
    # Opening the main file to read it
    with open(main_file, 'r') as f:
        count = 0
        lines = []

        # Index file to store the indexes
        index_file = {}

        for line in f:
            
            # Incrementing the count and appending the line
            count += 1
            lines.append(line)
            
            # If the count reaches the chunk size then create a file
            if count % chunk_size == 0:
                # Creating the file name to store the chunks file
                file_name = chunks_file_name + str(int(count / chunk_size)) + '.csv'

                # Writing the chunk into a new file
                write_chunk(file_name, lines)
                
                # Adding the first record of file to the index file
                index_file = { file_name: lines[0].strip().split(",")[key] } | index_file

                # Resetting the lines to an empty array
                lines = []
        
        # write remainder
        if len(lines) > 0:
            # Creating file name for the new file
            file_name = chunks_file_name + str(int(count / chunk_size) + 1) + '.csv'

            # Adding the first record of file to the index file
            index_file = { file_name: lines[0].strip().split(",")[key] } | index_file

            # Writing the chunk into a new file
            write_chunk(file_name, lines)
        
        # Returning the index file
        return index_file

# This function writes the chunk into a file
def write_chunk(file_name, lines):
    with open(file_name, 'w') as f_out:
        f_out.writelines(lines)
        