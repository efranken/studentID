students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def save_file(student):
        try:
            f = open("students.txt", "a")
            f.write(student + "\n")
            f.close()
        except Exception as error:
            print("Could not save file", error)


def read_file():
        try:
            f = open("students.txt", "r")
            for student in f.readlines():
                    add_student(student)
            f.close()
        except Exception as error:
                print("Could not read file", error)


read_file()
print_students_titlecase()

student_name = input("enter student name: ")
student_id = input("enter student id: ")

add_student(student_name, student_id)
save_file(student_name)


#
# def input_student():
#     x = "yes"
#     while x == "yes":
#         yes_no =  input("Would you like to enter a student?")
#
#         if yes_no == "yes":
#             student_name = input("enter student name: ")
#             student_id = input("enter student ID: ")
#
#         if yes_no != "yes":
#             x = "who cares what's in here"
#
#     add_student(student_name, student_id)
#     print_students_titlecase()
#
# input_student()