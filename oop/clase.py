"""
Clase in OOP
Clasa = un tip de date
O clasa ofera un mod de a grupa date (variabile) si functii intre care exista o
legatura logica descriind proprietatile si comportamentul unor entitati din
lumea reala.
Clasa = un sablon / template / blueprint care specifica datele si
        comportamentul instantelor create pe baza acestui sablon.
Sintaxa:
class Nume_clasa:
    instructiuni
Conventie: numele clasei incepe cu litera mare
In Python exista:
    - clase built-in (int, str, list, etc)
    - clase user-defined (definite de utilizator)
Clasele au membri:
    - atribute / proprietati - caracteristici care descriu starea
    - metode (functii) - care descriu comportamentul - modifica stare
"""
from admin_cont_oop import Cont


class Angajat:
    def __init__(self, nume, salariu, varsta):
        self.nume = nume    # membru (atribut) public
        self.__salariu = salariu    # membru private (in int. clasei)
        self._varsta = varsta   # membru protected (in int. package)

    def info(self):
        print(f'Angajat {self.nume}, varsta {self._varsta}')

    def arata_sal(self):
        print(f'Salariul lui {self.nume}: {self.__salariu} ')


class Cursant:
    def __init__(self):
        self.curs = "Python Developer"

    def info(self):
        print(f'Cursantul este inscris la cursul {self.curs}')


class Student:
    """Creeaza un obiect de tip student
        Atribute: nume, age
        Metode: info
    """
    nr_studenti = 0

    def __init__(self, name, age=19):
        self.name = name
        self.age = age
        # Student.nr_studenti += 1
        __class__.nr_studenti += 1

    def info(self):
        print(f'Studentul {Student.makeTitle(self.name)}, varsta {self.age}')

    @staticmethod
    def makeTitle(string):
        """Converteste stringul in titlu
        """
        return string.title()


class Calcule:
    """
    Clasa cu metode de calcul statice
    """
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Impartire la zero"

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def square(z):
        return z**2


def main():
    un_student = Student("John Doe", 19)
    # print(un_student)
    # print(type(Student))
    # print(type(un_student))
    un_student.info()
    print(f'Numele studentului este: {un_student.name}')
    # alt_student = Student("Alex Sima", 20)

    my_list = list()
    my_list.append(4)
    print(f'Lista este: {my_list}')

    un_cont = Cont("John D", 100)
    un_cont.arata_stare()


if __name__ == '__main__':
    main()
