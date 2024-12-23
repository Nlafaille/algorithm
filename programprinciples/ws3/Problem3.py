integer1 = int(input('Integer 1? '))
integer2 = int(input('Integer 2? '))
integer3 = int(input('Integer 3?' ))

if integer1 > integer2:
    integer1, integer2 = integer2, integer1
if integer1 > integer3:
    integer1, integer3 = integer3, integer1
if integer2 > integer3:
    integer2, integer3 = integer3, integer2

# Print the integers in descending order
print("Sorted:", integer3, integer2, integer1)

