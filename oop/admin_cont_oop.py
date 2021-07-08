"""
Programare orientata pe obiecte (Object oriented programming)
Paradigma de programare = un model mental, un mod de a organiza un program
Programare procedurala = organizam codul dupa pasii pe care ii executam
    pentru a rezolva o problema

Programare orientata pe obiecte (OOP) = organizam codul in jurul claselor si
    obiectelor
    = modeleaza entitati din lumea reala pe baza caracteristicilor si
    functionalitatilor acestora

Problema de rezolvat = administrarea unui cont
 - crearea unui cont bancar (nume titular, total cont)
 - afisarea starii contului
 - depunerea unei sume in cont
 - retragerea unei sume din cont
"""


class Cont:
    def __init__(self, nume, total):
        self.nume = nume
        self.total = total

    def arata_stare(self):
        print(f'In contul {self.nume} totalul este: {self.total}')

    def depune(self, depunere):
        self.total += depunere
        print(f'Am depus in contul {self.nume} suma {depunere}')

    def retrage(self, retragere):
        if retragere > self.total:
            print(f'Fonduri insuficiente in contul {self.nume}')
        else:
            self.total -= retragere
            print(f'Am retras suma de {retragere} din contul {self.nume}')


def main():
    cont1 = Cont("John Doe", 200)
    cont1.arata_stare()
    cont1.depune(245)
    cont1.arata_stare()
    cont1.retrage(100)
    cont1.arata_stare()
    cont1.retrage(2100)
    cont1.arata_stare()


if __name__ == "__main__":
    main()
