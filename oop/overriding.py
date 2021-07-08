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

Overriding  = supradefinirea metodelor
            = mecanismul prin care o subclasa redefineste o metoda deja
            definita in clasa parinte (de baza), schimbandu-i sau extinzandu-i
            comportamentul
Super()     - referinta la superclasa
            - nu mai e necesar sa folosim Nume_superclasa.metoda
            (self, atribute) ci doar super().metoda(atribute)
            - permite apelarea metodelor superclasei, inclusiv accesarea
            constructorului superclasei
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f'{self.name}, varsta {self.age} cu salariu {self.salary}')

    def get_salary(self):
        return self.salary


class Developer(Employee):
    def __init__(self, name, age, salary, language):
        # Employee.__init__(self, name, age, salary)
        super().__init__(name, age, salary)
        self.language = language

    def info(self):
        super().info()
        print(f'Language {self.language}')

    def extra_info(self):
        print(f'Sunt o instanta Developer {self.language}')


def main():
    emp = Employee("John Doe", 20, 2000)
    emp.info()
    dev = Developer("Alex Sima", 30, 3000, 'Python')
    dev.info()  # apelat metoda la nivelul insantei clasei derivate
    dev.extra_info()
    print(dev.salary)
    # help(Employee)
    help(Developer)


if __name__ == '__main__':
    main()
