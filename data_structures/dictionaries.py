"""
Dictionary (dictionar)  -   o colectie neordonata de perechi de tipul cheie si
                            valoare, unde cheile sunt unice
                        -   structura de date de tip mapping - realizeaza o
                            corespondenta intre chei si valori
Dictionary - structura de date mutable (schimbabil)
Cheile dictionarului trebuie se fie immutable (nemutabile)

Declarare dictionar:
    - elementele (perechi cheie valoare) separate prin virgula si incadrate
    intre acolade { }
    - constructorul dict()
Accesare elemente dictionar
    - pe baza numelui urmate de cheie intre []
    nume_dict[cheie]
    - cu metoda get(cheia_cautata) - returneaza valoarea asociata unei chei sau
                                    None daca nu exista in cheile dictionarului
Adaugarea unui element sau a mai multora:
    - un singur element se poate adauga folosind nume_dictionar[cheie]
        - in cazul in care cheia exista deja, se actualizeaza valoarea cu noua
        valoare
    - mai multe elemente cu metoda update()
Stergere elemente:
    - stergerea unui item (o pereche)
    del nume_dict(cheie)
    - stergerea in intregime a continutului - clear()
    - pop(cheie) -  stergerea unui element pe baza unei chei si returneaza
                    valoarea asociata cheii
    - popitem() - stergerea unui element si returneaza perechea cheie-valoare
                - pana la Python 3.7 elementul era aleatoriu, incepand cu 3.7
                este scos ultimul element adaugat
Parcurgerea elementelor unui dictionar:
- iterarea intr-o bucla for peste chei - afiseaza cheile
    for key in nume_dictionar:
        instructiuni
    - similar cu for key in nume_dictionar.keys()
- iterarea peste valori cu metoda values()
    for value in nume_dictionar.values()
        instructiuni
- iterarea peste elemente (perechi cheie valoare) cu metoda items()
    for key, value in nume_dictionar.items():
        instructiuni
"""

d = {}  # empty dictionary
d1 = {0: 'Python', 1: 'Git', 2: 'VSC'}
print(f'Numarul de elemente al dictionarului {d1} este {len(d1)}')
print(f'Tipul structurii de date: {type(d1)}')
developer = {'name': 'John Doe', 'age': 33, 'language': 'Python'}
print(f'Dictionarul developer este {developer}')

skills = dict(language='Python', name='Max', seniority=6)
print(f'Dictionarul creat prin mapare este: {skills}')

print(f'Valoarea din {d1} asociata cheii {1} este: {d1[1]}')
print(f'Valoarea din {developer} asociata cheii {"age"} este '
      f'{developer["age"]}')

print(f'Valoarea corespunzatoare cheii nume din dictionarul {developer}: '
      f'{developer.get("names")}'
      )
d1[3] = 'Github'
print(f'Dictionarul actualizat este: {d1}')
d1[2] = 'Visual Studio Code'
print(f'Dictionarul actualizat este: {d1}')
d1.update({5: 'JS', 6: 'Win10', 0: 'Python 3.9'})
print(f'Dictionarul actualizat este: {d1}')
developer.update(location='Bucuresti')
print(f'Dictionarul dupa actualizare cu update: {developer}')
# del developer['name']
# print(f'Dicitionarul developer dupa stergere item: {developer}')
dev_age = developer.pop('age')
print(f'Dictionarul dupa apelare pop: {developer}')
print(f'Valoarea asociata cheii age: {dev_age}')
# element = developer.popitem()
# print(type(element))
# print(f'Elementul scos este {element} iar dictionarul este: {developer}')
# elem_key = element[0]
# elem_value = element[1]
# elem_key, elem_value = element  # tuple unpacking
# print(f'Elementul sters din dictionar: {elem_key} : {elem_value}')
# del developer
for key in developer.keys():
    print(key)
for valoare in developer.values():
    print(valoare)
for key, value in developer.items():
    print(f'{key} : {value}')

dev2 = developer.copy()
print(f'{dev2}')
dev2.setdefault('country', 'Romania')
print(dev2)
