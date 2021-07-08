"""
Set (multime)   - un tip de date built-in care stocheaza o colectie neordonata
                de elemente unice, schimbabila (mutabila)
                - similar ca notiune multimii din matematica
                - permite operatii cu multimi
                    - reuniunea union()
                    - intersectia intersection()
                    - diferenta difference()
                    - diferenta simetrica symmetric_difference() - returneaza
                    un set cu valorile care sunt doar in una din cele doua
                    multimi
Creare (declarare variabila de tip set):
    - preciza elementele, separate prin virgula, intre acolade {}
    - constructor set()
Elementele duplicate sunt eliminate la creare.
Tipul de date set stocheaza o colectie neindexata (neordonata).
Adaugare elemente:
    add()       - permite adaugarea unui singur element (daca nu exista deja)
    update()    - permite adaugarea mai multor elemente
Stergere elemente:
    pop()           - sterge un element din set si il returneaza
    remove(item)    - sterge elementul dat ca parametru (KeyError daca nu
                    exista in set)
    discard(item)   - exact ca remove(), nu genereaza eroare daca elementul nu
                    exista in set
    clear()         - sterge toate elementele, setul devine gol (empty)
    del             - sterge variabila
Operatorul de apartenenta (membership) in / not in - verificare existenta item
in set
Copierea in intregime a unui set    - copy()
"""

my_set = set()     # empty set
set1 = {4, 8, 20, 4, 20, 1, 5}
print(f'Setul este: {set1}')
print(f'Tipul de date este: {type(set1)}')
set2 = set({3, 8, 9})
print(f'Al doilea set este: {set2}')
print(f'Numarul de elemente al setului {set1} este: {len(set1)}')

for item in set2:
    print(item)

lst = [5, 7, 6]
lst.append(9)
print(f'Lista este: {lst}')

set2.add(10)    # adauga un element la set
set2.add(9)     # elemente deja existente nu se mai adauga
print(f'Setul dupa adaugarea a doua valori: {set2}')
set2.update({20, 30, 40})
print(f'Setul dupa adaugarea a trei valori simultan cu update: {set2}')
set2.update(lst)
print(f'Setul dupa adaugarea elementelor listei {lst} este: {set2}')
valoare_stearsa = set2.pop()
print(f'Am scos valoarea {valoare_stearsa} cu pop din {set2}')
set2.remove(9)
print(f'Setul dupa stergerea valorii 9 este: {set2}')
# set2.remove(33)
set2.discard(20)
print(f'Setul dupa eliminarea valorii 20 este: {set2}')
# set2.clear()
print(f'Setul dupa apelarea metodei clear: {set2}')
# del set2
# print(set2)
# set2.pop()
if 5 in set2:
    print(f'Valoarea 5 este in {set2}')
else:
    print(f'Valoarea 5 nu este in {set2}')
# print(20 in set2)
s3 = set2.copy()
print(f'Setul obtinut prin copiere in totalitate: {s3}')
a = {4, 7, 9, 2}
b = {12, 6, 4, 1, 100}
print(f'{a} reunit cu {b}: {a.union(b)}')
print(f'{a} intersectat cu {b}: {a.intersection(b)}')
print(f'{a} - {b}: {a.difference(b)}')
print(f'{a} diferenta simetrica {b}: {a.symmetric_difference(b)}')

print(f'{a} este un subset al lui {{4, 2, 9}}: {a.issubset({4, 2, 9})}')
print(f'{a} este un subset al lui {{4, 2, 9, 7, 10}}: '
      f'{a.issubset({4, 2, 9, 7, 10})}')
t = (4, 6, 3, 4, 6, 6, 0)
new_set = set(t)
print(f'Setul obtinut prin conversie cu constructorul set este: {new_set}')
