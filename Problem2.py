file_name = input("File name: ")

with open(file_name) as input_name:
    lines = input_name.readlines()

#Get the first 2 lines:
first_two_lines = lines[:2]
last_two_lines = lines[-2:]

print("Output: ")
for line in first_two_lines:
    print(line.strip())
for line in last_two_lines:
    print(line.strip())
