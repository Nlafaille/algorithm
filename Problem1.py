source_file_name = input(f"Source file name: ")
target_file_name = input(f"Target file name: ")

with open(source_file_name, 'r') as source_file, open(target_file_name, 'w') as target_file: 

    for line in source_file:
        #strip() function
        if line.strip(): 
            target_file.write(line)
f = open(target_file_name, "r")
print("New text file:\n",f.read())
 