class Person:
    university_name = "Codegnan University"   # Class Attribute

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Student ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course, Year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.Year_ = Year_

        Student.student_count += 1

    def display_info(self):
        print("\n------ Student Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.__student_id)
        print("Course     :", self.course)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :", cls.student_count)

 # ---------------- Faculty ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Faculty ID :", self.__faculty_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :", cls.faculty_count)
        
# ---------------- Library ---------------- #

class Library:
    total_books = 5000

    def __init__(self, library_name):
        self.library_name = library_name
        self.issued_books = {}

    def issue_book(self, student, book_name):
        self.issued_books[student.name] = book_name
        print(f"{book_name} issued to {student.name}")

    def return_book(self, student):
        if student.name in self.issued_books:
            print(f"{student.name} returned {self.issued_books[student.name]}")
            del self.issued_books[student.name]
        else:
            print("No book issued.")

    def display_library(self):
        print("\n------ Library Details ------")
        print("Library Name :", self.library_name)
        print("Total Books  :", Library.total_books)
        print("Books Issued :", self.issued_books)

# ---------------- Non-Teaching Staff ---------------- #

class NonTeachingStaff(Person):
    staff_count = 0

    def __init__(self, name, age, staff_id, role, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__staff_id = staff_id
        self.role = role

        NonTeachingStaff.staff_count += 1

    def display_info(self):
        print("\n------ Non-Teaching Staff ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Staff ID   :", self.__staff_id)
        print("Role       :", self.role)
        print("Department :", self.Department)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)

    @classmethod
    def total_staff(cls):
        print("Total Non-Teaching Staff :", cls.staff_count)

# ---------------- Course ---------------- #

class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def display_course(self):
        print("\n------ Course Details ------")
        print("Course Name :", self.course_name)
        print("Duration    :", self.duration)
        print("Fee         :", self.fee)

# ---------------- Classroom ---------------- #

class Classroom:
    def __init__(self, room_no, capacity):
        self.room_no = room_no
        self.capacity = capacity

    def display_classroom(self):
        print("\n------ Classroom ------")
        print("Room Number :", self.room_no)
        print("Capacity    :", self.capacity)

# ---------------- Hostel ---------------- #

class Hostel:
    hostel_count = 0

    def __init__(self, hostel_name, rooms):
        self.hostel_name = hostel_name
        self.rooms = rooms
        Hostel.hostel_count += 1

    def display_hostel(self):
        print("\n------ Hostel Details ------")
        print("Hostel Name :", self.hostel_name)
        print("Rooms       :", self.rooms)

    @classmethod
    def total_hostels(cls):
        print("Total Hostels :", cls.hostel_count)

# ---------------- Objects ---------------- #

student1 = Student("Rahul Sharma",21,"CNU12345","Computer Science",2026,"Intermediate","Male","IT")

student2 = Student("Ananya Reddy",22,"CNU67890","Data Science",2026,"Intermediate","Female","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45,"F001","AI & ML","PhD","Male")

faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","Cybersecurity","PhD","Female")

# Library
library = Library("Central Library")

library.issue_book(student1, "Python Programming")
library.issue_book(student2, "Data Science with Python")

# Non-Teaching Staff
staff1 = NonTeachingStaff(
    "Ramesh Kumar",
    38,
    "S001",
    "Lab Assistant",
    "Computer Science",
    "B.Sc",
    "Male"
)

staff2 = NonTeachingStaff(
    "Priya Devi",
    35,
    "S002",
    "Office Administrator",
    "Administration",
    "MBA",
    "Female"
)

# Course
course1 = Course("Python Full Stack", "6 Months", 45000)

# Classroom
classroom1 = Classroom("A-203", 60)

# Hostel
hostel1 = Hostel("Boys Hostel", 120)
hostel2 = Hostel("Girls Hostel", 100)

# ---------------- Output ---------------- #

student1.display_info()
student2.display_info()

print("\nStudent ID:", student1.get_student_id())

faculty1.display_info()
faculty2.display_info()

Faculty.university_policy()

Student.total_students()
Faculty.total_faculty()

library.display_library()

staff1.display_info()
staff2.display_info()

course1.display_course()

classroom1.display_classroom()

hostel1.display_hostel()
hostel2.display_hostel()

library.return_book(student1)

NonTeachingStaff.total_staff()
Hostel.total_hostels()
