"""Instance variables vs static variables
Instance variable (OOP)= variabile declarate in interiorul metodelor clasei
    = (variabila a instantei) va defini atributele instantei
Static variables (OOP) = variabile declarate la nivelul clasei, in afara
    metodelor, care pot fi accesate direct folosind numele clasei
    = (variabile statice)
Variabilele statice se folosesc / acceseaza cu numele clasei
"""
from clase import Student

student = Student("John")
print(f'Numele studentului este: {student.name}')
al_doilea_student = Student("Max", 30)
print(f'Nr de studenti este: {Student.nr_studenti}')
