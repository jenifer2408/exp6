print("URK24CS1054")
print("SARO FRANZIKA")
print("University ERP System")
class Student:
    def __init__(self, student_id, name, dob, email, courses=[]):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.email = email
        self.courses = courses

    def enroll_course(self, course):
        self.courses.append(course)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Courses: {', '.join([course.course_name for course in self.courses])}"


class Course:
    def __init__(self, course_id, course_name, credits, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.instructor = instructor
        self.enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)
        student.enroll_course(self)

    def drop_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.drop_course(self)

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Credits: {self.credits}, Instructor: {self.instructor.name}"


class Staff:
    def __init__(self, staff_id, name, position, email):
        self.staff_id = staff_id
        self.name = name
        self.position = position
        self.email = email

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}, Position: {self.position}, Email: {self.email}"


class UniversityERP:
    def __init__(self):
        self.students = []
        self.courses = []
        self.staff = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_staff(self, staff):
        self.staff.append(staff)

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def get_staff(self, staff_id):
        for staff_member in self.staff:
            if staff_member.staff_id == staff_id:
                return staff_member
        return None

    def __str__(self):
        student_list = "\n".join(str(student) for student in self.students)
        course_list = "\n".join(str(course) for course in self.courses)
        staff_list = "\n".join(str(staff_member) for staff_member in self.staff)
        return f"University ERP System:\nStudents:\n{student_list}\nCourses:\n{course_list}\nStaff:\n{staff_list}"

# Create Staff Members
staff1 = Staff(staff_id=1, name="Dr. Aishaa", position="Professor", email="aishaa@university.com")
staff2 = Staff(staff_id=2, name="Mr. Edward", position="Assistant Professor", email="edward@university.com")

# Create Courses
course1 = Course(course_id=101, course_name="Computer Science 101", credits=3, instructor=staff1)
course2 = Course(course_id=102, course_name="Mathematics 101", credits=4, instructor=staff2)

# Create Students
student1 = Student(student_id=1001, name="Jenisha", dob="2005-02-01", email="jenishaa@student.com")
student2 = Student(student_id=1002, name="Casper John", dob="2004-05-20", email="casper.john@student.com")

# Create University ERP System
university_erp = UniversityERP()

# Add staff, courses, and students to ERP
university_erp.add_staff(staff1)
university_erp.add_staff(staff2)
university_erp.add_course(course1)
university_erp.add_course(course2)
university_erp.add_student(student1)
university_erp.add_student(student2)

# Enroll students in courses
course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student1)

# Print all information
print(university_erp)

# Example of dropping a course for a student
course1.drop_student(student1)

# Print updated information
print("\nUpdated Information after dropping course:")
print(university_erp)
