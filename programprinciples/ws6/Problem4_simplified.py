def convert_string_to_list(student_grades):
    integer_list = []
    for item in student_grades:
        integer_list.append(int(item))
    return integer_list

def get_student_average_scores(student_grades):
    average_scores=[]
    for element in student_grades:
        current_student_avg_score = sum(element) / len(element)
        average_scores.append(current_student_avg_score)
    return average_scores

def get_course_average_scores(student_grades):
    average_scores=[]
    for i in range(len(student_grades[0])):# i represents course id
        course_sum = 0
        for j in range(len(student_grades)):# j represents student id
            course_sum = course_sum +student_grades[j][i]
        average_scores.append(course_sum/len(student_grades))
    return average_scores


number_of_course = 4
number_of_student = 5
while True:
    student_grades = []
    for i in range(number_of_student):
        current_student_grades = input("Enter marks for Student (or press Enter to quit): ").split()
        current_student_grades = convert_string_to_list(current_student_grades)
        student_grades.append(current_student_grades)
    print(student_grades)
    student_average_scores = get_student_average_scores(student_grades)
    course_average_scores = get_course_average_scores(student_grades)
    print(f"The highest average mark of students:", max(student_average_scores))
    print(f"The highest average mark of courses:", max(course_average_scores))
