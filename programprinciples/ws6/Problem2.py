while True:

    #Get input from the user
    given_list1 = input("List 1: ").split()
    given_list2 = input("List 2: ").split()

    #Convert list of string to integers
    integer_list1 = []
    for item in given_list1:
        integer_list1.append(int(item))

    integer_list2 = []
    for item in given_list2:
        integer_list2.append(int(item))

    #calculate the sum of the first and the last integer

    sum1 = integer_list1[0] + integer_list1[-1]  # Add the first and last elements of list1
    sum2 = integer_list2[0] + integer_list2[-1]  # Add the first and last elements of list2

    # Step 4: Compare the sums and print the result
    if sum1 > sum2:
        print(sum1)
    elif sum1 < sum2:
        print(sum2)
    else:
        print("Same")