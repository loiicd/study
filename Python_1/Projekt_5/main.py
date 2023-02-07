import json
from classes import *
import functions as f

# --- Students Data Json ---
file = open("/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python/Projekt_5/students.json", "r")
students_data = json.load(file)

# --- Professor Data Json ---
file = open("/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python/Projekt_5/professors.json", "r")
professors_data = json.load(file)

# ----------------
# --- Students ---
# ----------------
students = []
for student in students_data:
  students.append(Student(name = student["name"], 
                      cours = student["cours"], 
                      age = student["age"], 
                      hobby = student["hobby"], 
                      grade = student["grade"]))

# ------------------
# --- Professors ---
# ------------------
professors = []
for professor in professors_data:
  professors.append(Professor(name = professor["name"], 
                              subjects = professor["subjects"]))





while True:
  print()
  input_value = input("Eingabe: ").lower()
  match input_value:
    # *** help ***
    case "help" | "hilfe":
      f.print_ux_star("Hilfe:", "Benoten       Einen Studenten benoten")

    # *** grading ***
    case "benoten":
      student_input = input("Student: ")
      grade = input("Note: ")
      for student in students:
        if student.name == student_input:
          Professor.grade_student(student, grade)

    # *** show students ***
    case "studenten anzeigen":
      print()
      print("Studenten:")
      for student in students:
        print(f"Name: {student.name} Note: {student.grade}")

    # *** exit programm ***
    case "beenden":
      f.print_ux_star("", "Programm wurde beendet!")
      break

    # *** Wrong input ***
    case other:
      f.print_ux_star("", "Befehl exestiert nicht!")