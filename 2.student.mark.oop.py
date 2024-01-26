class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__id = student_id
        self.__name = student_name
        self.__dob = student_dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob


class Course:
    def __init__(self, course_id, course_name):
        self.__id = course_id
        self.__name = course_name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class MarksManager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        return Student(student_id, student_name, student_dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        if student_id not in self.students or course_id not in self.courses:
            print("Invalid student ID or course ID.")
            return

        mark = float(input("Enter mark for {}: ".format(self.students[student_id].get_name())))
        self.marks[(student_id, course_id)] = mark

    def list_courses(self):
        print("\nList of Courses:")
        for course_id, course in self.courses.items():
            print("ID: {}, Name: {}".format(course_id, course.get_name()))

    def list_students(self):
        print("\nList of Students:")
        for student_id, student in self.students.items():
            print("ID: {}, Name: {}, DoB: {}".format(student_id, student.get_name(), student.get_dob()))

    def show_student_marks(self):
        course_id = input("Enter course ID: ")

        if course_id not in self.courses:
            print("Invalid course ID.")
            return

        print("\nMarks for Course '{}':".format(self.courses[course_id].get_name()))
        for (student_id, c_id), mark in self.marks.items():
            if c_id == course_id:
                student_name = self.students[student_id].get_name()
                print("Student ID: {}, Student Name: {} Mark: {}".format(student_id, student_name, mark))

    def run(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            student_info = self.input_student_info()
            self.students[student_info.get_id()] = student_info

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            course_info = self.input_course_info()
            self.courses[course_info.get_id()] = course_info

        while True:
            print("\nMenu:")
            print("1. Input student marks for a course")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.input_student_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    marks_manager = MarksManager()
    marks_manager.run()
