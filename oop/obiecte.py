"""
Objects in OOP
Clasa = un tip de date (un template / un blueprint)
Obiect = o instanta a unei clase (o instanta a unui tip de date)

In Python aproape orice este un obiect

Obiect ~ componenta logica prin intermediul careia modelam o entitate reala
    care detine:
    - identitate - definita prin nume
    - stare - definita prin atribute (proprietati)
    - comportament - definit prin metode
"""
from clase import Student


def double(value):
    return 2 * value


un_student = Student("John", 18)
print(un_student)
un_student.info()
new_list = [4, 6, 7]
print(new_list.count(6))
