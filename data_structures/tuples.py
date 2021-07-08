"""
Tuple (tuplu) = tip de date similar listei
                o colectie de elemente ordonata (indexata), permite duplicate,
                neschimbabila (un tip de date immutable - nu se poate modifica
                dupa creare)
                - permite duplicate
Declarare, asemanator listei dar folosim () in loc de []
nume_tuplu = (element1, element2, ...)
Accesare elemente: indexing, slicing, pozitia (indexul) porneste de la 0
Avantaje:
    - viteza de calcul (performanta)
    - securitate (datorita faptului ca este immutable)
Tuple este immutable    - nu se pot adauga / elimina elemente
                        - nu se poate realiza reasignarea unui element
Concatenare - lipirea a doua obiecte de tip tuple cu operatorul +
            (ca la string)
Sortare - metoda sorted() care returneaza un nou tuplu cu elementele sortate
"""

lista = [4, 6, 8, 12, 3, 6, 11]
tuplu = (4, 6, 11, 0, 22, 33, 112, 5, 11, 0, 9)
print(f'Tipul de date tuplu: {type(tuplu)}')
print(f'Ultimul element al tuplului este: {tuplu[-1]}')
print(f'Al doilea element al tuplului este: {tuplu[1]}')
print(f'Numarul de elemente al tuplului este: {len(tuplu)}')
print(f'Primele 3 elemente obtinute prin slicing: {tuplu[:3]}')
# t = tuplu[:3]
# print(type(t))
new_tup = tuple([0, 3, 6])
print(new_tup)
# new_tup[2] = 1  # TypeError, nu suporta asignarea elementelor
tuplu = (7, 20, 5, 29)
print(7 in tuplu)
print(20 not in tuplu)
value = 20
if value in tuplu:
    print(f'Valoarea {value} este in tuplul {tuplu}')
else:
    print(f'Valoarea {value} nu este in tuplu {tuplu}')
for item in tuplu:
    print(item)
tup3 = tuplu + new_tup
print(f'Concatenand {tuplu} cu {new_tup} obtinem {tup3}')
lista.sort()
print(lista)

s = sorted(tup3)
print(f'Sortand elementele {tup3} obtinem {s}')
print(f'Numarul de aparitii al valorii 3 in {tup3} este {tup3.count(3)}')
print(f'Pozitia elementului 3 in tuplul {tup3} este {tup3.index(3)}')
skills = ('Python', 'Visual Studio Code', 'Git', 'Github', ['programare',
                                                            'debugging'])
print(skills[1])
