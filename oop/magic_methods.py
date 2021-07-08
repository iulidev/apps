"""
Magic methods = metode speciale (dunder methods) care incep si se termina cu __
                dunder = Double UNDERscore
                nu sunt chemate explicit de catre programator, sunt menite sa
                fie apelate atunci cand se realizeaza anumite actiuni
                - apelarea magic methods se realizeaza automat, intern
Un exemplu      __init__ (constructor) - executata atunci cand instantiem
                clasa
                __str__ genereaza reprezentarea ca string a obiectului folosita
                implicit cand apelam print(obiect) - informala
                __repr__ reprezentarea oficial ca string a instantei (toate
                informatiile despre obiect)
Avantajul magic methods = operator overloading
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee({self.name}, {self.age}, {self.salary})'

    def __add__(self, other):
        """
        Operatorul + determina suma salariilor
        Aplicat asupra a doua obiecte ale clasei
        """
        return self.salary + other.salary

    def display(self):
        print(f'{self.name}, {self.age}, {self.salary}')


def main():
    emp1 = Employee("John Doe", 45, 2000)
    # emp1.display()
    emp2 = Employee("Max Doe", 50, 4000)
    print(f'Aplicand operatorul + asupra a doi angajati: {emp1 + emp2}')
    print(emp1)
    # print(str(emp1))


if __name__ == '__main__':
    main()
