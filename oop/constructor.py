"""
Constructor = metoda clasei cu rolul de a instantia un obiect
            - are rolul de a crea o instanta (obiect) initializand parametrii
            (atributele) cu valori concrete
De fiecare data cand cream un obiect al clasei este apelat constructorul.
In Python metoda __init__ este constructorul.
Constructorii sunt de doua tipuri:
    - default
    def __init__(self):
    - parametrizat
    def __init__(self, parametru1, parametru2, ...)
Self keyword - o referinta la instanta creata cand instantiem o clasa
             - o referinta la obiectul creat
Dunder method (Double UNDERscore method) - metoda speciala in Python 
            care are un rol predefinit

"""
from clase import Student, Cursant


un_student = Student("John", 18)
print(un_student)
un_student.info()
# new_list = [4, 6, 7]
# print(new_list.count(6))
cursant1 = Cursant()
print(cursant1.curs)
cursant2 = Cursant()
print(cursant2.curs)
