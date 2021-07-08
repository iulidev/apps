"""
Interface (interfata)   = o descriere a atributelor si comportamentului unui
                        tip de obiecte
                        = o lista de declaratii de metode, nu si implementari
                        (specifica metodele fara a intra in detalii legate de
                        implementare)
In Python se pot defini interfete cu modulul abc din care importam clasa helper
ABC si decoratorul @abstractmethod
Reguli stricte pe care trebuie sa le respecte interfetele:
    - pot contine numai variabile statice (nu si instance variables)
    - numai metode abstracte (fara metode ale instantelor)
    - nu exista constructor in interfata
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


class Triunghi(Forma):
    def __init__(self, baza, inaltime, latura1, latura2):
        self.baza = baza
        self.inaltime = inaltime
        self.latura1 = latura1
        self.latura2 = latura2

    def arie(self):
        return (self.baza * self.inaltime) / 2

    def perimetru(self):
        return self.baza + self.latura1 + self.latura2


class Dreptunghi(Forma):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def arie(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)


def main():
    t = Triunghi(2, 5, 4, 2)
    print(f'Aria este: {t.arie()}')
    print(f'Perimetrul este: {t.perimetru()}')
    d = Dreptunghi(4, 5)
    print(f'Aria dreptungi :{d.arie()}')


if __name__ == '__main__':
    main()
