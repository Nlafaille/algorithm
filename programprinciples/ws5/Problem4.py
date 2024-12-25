import math
def compute_total_carpet_length(length, width):
    roll_carpet_size = 3.66

#Calculate carpet requirements
    widthways_carpet = math.ceil(length / roll_carpet_size) * width
    lengthways_carpet = math.ceil(width / roll_carpet_size) * length

    return widthways_carpet,lengthways_carpet

#Main program
while True:
    #inputs
    room_dimension1 = float(input("Enter room dimension 1 (m): "))
    room_dimension2 = float(input("Enter a room dimension2 (m): "))
    if room_dimension1 == 0 and room_dimension2 == 0:
        break
    #validate which one is length and width
    room_length = max(room_dimension1, room_dimension2)
    room_width = min(room_dimension1, room_dimension2)
    widthway_paid_meter,lengthway_paid_meter = compute_total_carpet_length(room_length,room_width)

    #Display results
    print(f"Length of room (longer side): {room_length:.3f} m")
    print(f"Width of room (shorter side): {room_width:.3f} m")
    print(f"Total carpet length required in lengthways manner = {lengthway_paid_meter} m")
    print(f"Total carpet length required in widthways manner = {widthway_paid_meter} m")
    print()



