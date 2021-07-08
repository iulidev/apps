"""
Inheritance (Mostenirea)
Inheritance = mecanismul prin care o clasa preia atributele(datele membre) si
comportamentul (metodele membre) unei alte clase, la care adauga membri
specifici

Clasa parinte (superclasa sau clasa de baza) = clasa de la care se preia
starea/proprietatile si comportamentul
Clasa copil (subclasa sau clasa derivata) = clasa care preia starea si
comportamentul

Sintaxa pentru definirea unei clase derivate (subclase):

class Nume_clasa_derivata(Nume_clasa_de_baza):
    instructiuni

Cand derivam o clasa pe baza unei clase aflata intr-un modul, extindem sintaxa:
class Nume_clasa_derivata(nume_modul.Nume_clasa_de_baza)
Avantaj inheritance: code reuse
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f'{self.name}, varsta {self.age} cu salariu {self.salary}')


class Developer(Employee):
    # pass
    def extra_info(self):
        print('Sunt o instanta Developer')


def main():
    emp = Employee("John Doe", 20, 2000)
    emp.info()
    dev = Developer("Alex Sima", 30, 3000)
    dev.info()  # apelat metoda la nivelul insantei clasei derivate
    dev.extra_info()
    print(dev.salary)
    # help(Employee)
    help(Developer)


if __name__ == '__main__':
    main()
