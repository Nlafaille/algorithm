def determine_g_state(text):
    for index in range(len(text)):
        if text[index] == "g":
            is_left_neighbour_g = index > 0 and text[index - 1] == "g"
            is_right_neighbour_g = index < len(text)-1 and text[index + 1] == "g"
            if not is_left_neighbour_g and not is_right_neighbour_g:
                return False
    return True
# def determine_g_state(text):
#     if len(text) == 1:
#         return False
#     for index in range(len(text)):
#         if text[index] == "g":
#             if index==0:
#                 if text[index + 1] != "g":
#                     return False
#             elif index == len(text)-1:
#                 if text[index-1]!="g":
#                     return False
#             else:
#                 if text[index + 1]!="g" and text[index - 1]!="g":
#                     return False
#     return True
# Main program
while True:
# inputs
    text = input("String: ")
    result = determine_g_state(text)
    if result:
        print("Happy?: True")
    else:
        print("Happy?: False")