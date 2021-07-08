"""Instance variables vs static variables
Instance variable (OOP)= variabile declarate in interiorul metodelor clasei
    = (variabila a instantei) va defini atributele instantei
Static variables (OOP) = variabile declarate la nivelul clasei, in afara
    metodelor, care pot fi accesate direct folosind numele clasei
    = (variabile statice)
Variabilele statice se folosesc / acceseaza cu numele clasei

Static methods  = metode definite in interiorul clasei fara a avea ca parametru
                instanta clasei (self care referentiaza obiectul)
                = functii utilitare care nu manevreaza instanta
                = se apeleaza cu numele clasei (fara obiect)
Decorator in Python pentru a defini metode statice:
                @staticmethod
Instance methods = metode care actioneaza asupra instantei
                - au self ca parametru
                * se pot crea clase doar cu functii statice ca un mod de a
                organiza codul
"""
from clase import Student, Calcule

student = Student("John")
print(f'Numele studentului este: {student.name}')
al_doilea_student = Student("Max", 30)
print(f'Nr de studenti este: {Student.nr_studenti}')
print(f'{Student.makeTitle("john doe")}')
student.info()

print(f'7 ridicat la patrat = {Calcule.square(7)}')
print(f'8 impartit la 2 = {Calcule.divide(8, 2)}')
