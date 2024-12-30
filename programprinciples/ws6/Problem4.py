def convert_string_to_list(student_grades):
    integer_list = []
    for item in student_grades:
        integer_list.append(int(item))
    return integer_list


while True:
    # collect input for the matrix
    student_1_grades = input("Enter marks for Student (or press Enter to quit): ").split()
    student_2_grades = input("Enter marks for Student (or press Enter to quit): ").split()
    student_3_grades = input("Enter marks for Student (or press Enter to quit): ").split()
    student_4_grades = input("Enter marks for Student (or press Enter to quit): ").split()
    student_5_grades = input("Enter marks for Student (or press Enter to quit): ").split()

    student_1_grades = convert_string_to_list(student_1_grades)
    student_2_grades = convert_string_to_list(student_2_grades)
    student_3_grades = convert_string_to_list(student_3_grades)
    student_4_grades = convert_string_to_list(student_4_grades)
    student_5_grades = convert_string_to_list(student_5_grades)

    student_grades = [student_1_grades, student_2_grades, student_3_grades, student_4_grades, student_5_grades]

    student_1_average = sum(student_1_grades) / 4
    student_2_average = sum(student_2_grades) / 4
    student_3_average = sum(student_3_grades) / 4
    student_4_average = sum(student_4_grades) / 4
    student_5_average = sum(student_5_grades) / 4

    highest_average_student_mark = max(student_1_average, student_2_average, student_3_average, student_4_average,
                                       student_5_average)
    print(f"The highest average mark of students:", highest_average_student_mark)
    course_1_sum = 0
    course_2_sum = 0
    course_3_sum = 0
    course_4_sum = 0
    for element in student_grades:
        course_1_sum = course_1_sum + element[0]
        course_2_sum = course_2_sum + element[1]
        course_3_sum = course_3_sum + element[2]
        course_4_sum = course_4_sum + element[3]

    average_mark_course_1 = course_1_sum / 5
    average_mark_course_2 = course_2_sum / 5
    average_mark_course_3 = course_3_sum / 5
    average_mark_course_4 = course_4_sum / 5

    highest_average_course_mark = max(average_mark_course_1, average_mark_course_2, average_mark_course_3,
                                      average_mark_course_4)
    print(f"The highest average mark of courses:", highest_average_course_mark)
