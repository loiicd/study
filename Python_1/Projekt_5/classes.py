import functions as f

class Student:
  def __init__(self, name: str, cours: str, age: int, hobby: str, grade: float):
    self.name = name
    self.cours = cours
    self.age = age
    self.hobby = hobby
    self.grade = grade

class Professor:
  def __init__(self, name: str, subjects: list):
    self.name = name
    self.subjects = subjects
  
  @staticmethod
  def grade_student(student: Student, grade: float):
    student.grade = grade 

class University:
  def __init__(self, name: str, location: str, rooms: list, courses: dict):
    self.name = name
    self.location = location
    self.rooms = rooms
    self.courses = courses


