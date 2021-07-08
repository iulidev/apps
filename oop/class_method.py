"""
Class method (metoda a clasei)
Instance method = o metoda a instantei (a obiectului)
                - o functie in interiorul clasei care manevreaza instanta si
                are ca prim parametru chiar instanta, accesat prin self
Class method    = o metoda a clasei
                - o functie in interiorul clasei care manevreaza clasa si are
                ca prim parametru chiar clasa, accesata prin cls
Class method se defineste cu decoratorul @classmethod
    @classmethod
    def nume_class_method(cls, enumerare_parametri):
"""

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name} {self.age}')

    @classmethod
    def from_year_of_birth(cls, name, year):
        return cls(name, date.today().year - year)


x = Person("John Doe", 20)
x.info()
p = Person.from_year_of_birth("Another Name", 1984)
p.info()
