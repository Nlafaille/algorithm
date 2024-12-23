
#Fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

number = int(input("Enter a number: "))

if number <= 0:
    print("provide a positive number")
elif number == 1:
    print("0")
elif number == 2:
    print("0 1")
elif number > 2:
    total_loops = number-2
    count = 1# indicate number of loops we have executed so far
    count_2 = 2# indicate number of numbers being printed
    x1 = 0
    x2 = 1
    print(x1, x2, end=" ")
    while True:
        if count > total_loops:
            break
        # calculate numbers
        current_number = x1 + x2 #
        x1 = x2#
        x2 = current_number #
        print(current_number, end=" ")
        count = count + 1
        count_2= count_2+1
        if count_2%4 == 0:
            print()


