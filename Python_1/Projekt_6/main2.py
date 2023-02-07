from datetime import *

today = date.today()

class Student:
  def __init__(self, name: str, birthdate: date):
    self.name = name
    self.__birthdate = birthdate
    self.age = today.year - birthdate.year
    self.grade = None

  def print_info(self):
    print()
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Grade: {self.grade}")

class Lecturer:
  def __init__(self, name: str, birthdate: date, students: list):
    self.name = name
    self.__birthdate = birthdate
    self.age = today.year - birthdate.year
    self.__students = students

  def grade_student(self):
    for student in self.__students:
      print(student.name)
      grade = input("Grade: ")
      student.grade = grade

  def show_grades(self):
    print("Grades:")
    for student in self.__students:
      print()
      print(f"Name: {student.name}")
      print(f"Grade: {student.grade}")

student1 = Student(name = "Max", birthdate = date(2002, 4, 13))
student2 = Student(name = "Sarah", birthdate = date(2003, 7, 20))
student3 = Student(name = "Tim", birthdate = date(2001, 2, 24))

lecturer1 = Lecturer(name = "Müller", birthdate = date(1976, 12, 1), students = [student1, student2, student3])

lecturer1.grade_student()
lecturer1.show_grades()
print()

