
while True:
    #Get input from user
    text = input("Enter a string: ")

    #Check if the input is empty (stop condition)
    if text == "":
        break

    # Check if string contains spaces, and temporarly removes spaces
    cleaned_text = text.replace(" ", "")
    if cleaned_text.isalpha():
        words = text.lower().split()
        words.sort(reverse=True)
        for word in words:
            print(word, end=" ")
        print()

    else:
        print("You must enter a string without digits or symbols in the string")

