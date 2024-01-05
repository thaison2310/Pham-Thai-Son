def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

def input_student_marks(students, courses, marks):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    if student_id not in students or course_id not in courses:
        print("Invalid student ID or course ID.")
        return

    mark = float(input("Enter mark for {}: ".format(students[student_id]['name'])))
    marks[(student_id, course_id)] = mark

def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course_info in courses.items():
        print("ID: {}, Name: {}".format(course_id, course_info['name']))

def list_students(students):
    print("\nList of Students:")
    for student_id, student_info in students.items():
        print("ID: {}, Name: {}, DoB: {}".format(student_id, student_info['name'], student_info['dob']))

def show_student_marks(marks, courses, students):
    course_id = input("Enter course ID: ")

    if course_id not in courses:
        print("Invalid course ID.")
        return

    print("\nMarks for Course '{}':".format(courses[course_id]['name']))
    for (student_id, c_id), mark in marks.items():
        if c_id == course_id:
            student_name = students[student_id]['name']
            print("Student ID: {}, Student Name: {} Mark: {}".format(student_id, student_name, mark))

def main():
    students = {}
    courses = {}
    marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student_info = input_student_info()
        students[student_info['id']] = student_info

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_info()
        courses[course_info['id']] = course_info

    while True:
        print("\nMenu:")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            input_student_marks(students, courses, marks)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(marks, courses, students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()