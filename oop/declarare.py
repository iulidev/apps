"""Declaring a class instance (object)
Declarare si instantiere = pentru a crea o instanta a unei clase apelam clasa
folosind numele clasei si transmitem argumentele ca in constructor (__init__)
"""
from clase import Student, Cursant

student = Student("John Doe", 30)
un_student = Student("Alt nume")
print(f'Studentul cu numele {student.name}')
print(f'Studentul cu numele {un_student.name}')
un_student.info()
Student("Max").info()
# help(Student)
cursant = Cursant()
cursant.info()
