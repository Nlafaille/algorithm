source_file = input(f"Source file name: ")
target_file = input(f"Target file name: ")
banned_word = input(f"Banned word: ")

number_of_lines = 0 

with open(source_file, 'r') as source, open(target_file, 'w') as target:
    for line in source:
        if banned_word not in line:
            target.write(line)
        else:
            number_of_lines += 1