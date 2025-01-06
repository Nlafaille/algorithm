source_file_name = input(f"Source file name: ")
target_file_name = input(f"Target file name: ")

removed_lines_count = 0 

with open(source_file_name, 'r') as source_file, open(target_file_name, 'w') as target_file: 

    for line in source_file:
        #strip() function means non empty
        if line.strip(): 
            target_file.write(line)
        else:
            #Increment the counter for removed lines
            removed_lines_count  += 1
print(f"Lines removed: {removed_lines_count}")
 