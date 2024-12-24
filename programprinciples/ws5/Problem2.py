def char_replacement(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += "_"
        else:
            result += char
    return result

user_input = input("Enter a string: ")
output = char_replacement("user_input")
print(output)
