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
nume_cont1 = "John Doe"
total_cont1 = 200


def arata_stare(nume_cont, total_cont):
    print(f'In contul {nume_cont} totalul este: {total_cont}')


def depune_in_cont(nume_cont, total_cont, depunere):
    total_cont += depunere
    print(f'Am depus in contul {nume_cont} suma {depunere}')
    return total_cont


def retrage_din_cont(nume_cont, total_cont, retragere):
    if retragere > total_cont:
        print(f'Fonduri insuficiente in contul {nume_cont}')
    else:
        total_cont -= retragere
        print(f'Am retras suma de {retragere} din contul {nume_cont}')
    return total_cont


def main():
    global total_cont1, nume_cont1
    arata_stare(nume_cont1, total_cont1)
    total_cont1 = depune_in_cont(nume_cont1, total_cont1, 245)
    arata_stare(nume_cont1, total_cont1)
    total_cont1 = retrage_din_cont(nume_cont1, total_cont1, 100)
    arata_stare(nume_cont1, total_cont1)
    total_cont1 = retrage_din_cont(nume_cont1, total_cont1, 2100)
    arata_stare(nume_cont1, total_cont1)


if __name__ == "__main__":
    main()
