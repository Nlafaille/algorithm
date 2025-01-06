source_file_name = input("Source file name: ")

with open(source_file_name, 'r') as source_file:
    source_file_contents = source_file.read()