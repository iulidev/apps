""" Abstract base classes
Clase abstracte     - permit o generalizare, crearea unui template generic
                    (clasa generica)
Metoda abstracta    = o metoda a clasei care este declarata (definita) fara
                    a contine (obligatoriu) implementare
                    = identificata cu decoratorul @abstractmethod
Clasa abstracta = o clasa care contine una sau mai multe metode abstracte
Clasele abstracte respecta regulile:
    1. nu pot fi instantiate
    2. toate metodele abstracte trebuie supradefinite (prin method overriding)
Clasa abstracta = o clasa care reprezinta o generalizare si prevede metodele
dar este creata pentru a fi extinsa (mostenita) si nu instantiata

"""

from abc import ABC, abstractmethod


class AbstractClsExample(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def show_data(self):
        pass

    def another_method(self):
        print('Aceasta este o metoda a clasei care nu e abstracta')


class ExtendedClass(AbstractClsExample):
    def info(self):
        print('Mesaj din metoda info, supradefinita')

    def show_data(self):
        print('Mesaj din metoda show_data, supradefinita')


class Forma_geometrica(ABC):
    @abstractmethod
    def aria(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


class Patrat(Forma_geometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura**2

    def perimetru(self):
        return self.latura * 4


def main():
    # c = AbstractClsExample() # TypeError - nu poate fi instantiata
    e = ExtendedClass()
    e.show_data()
    e.info()
    e.another_method()
    # f = Forma_geometrica()
    patrat = Patrat(5)
    print(f'Aria patratului este: {patrat.aria()}')
    print(f'Perimetrul patratului este: {patrat.perimetru()}')


if __name__ == '__main__':
    main()
