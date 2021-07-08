"""
Map function (functia map)
Functia map() aplica o functie data ca parametru fiecarui element al unei
colectii (iterabil) si intoarce o colectie cu rezultatele obtinute (de tip
map)
Sintaxa:
    map(functie, colectie,...)
    - pot fi transmise una sau mai multe colectii ca parametru
Pentru accesarea elementelor obiectului de tip map (iterator) folosim:
- casting (conversie) de exemplu la list sau set
- for (iterare intr-o bucla for)
Avantaje:
    - un mod facil de a procesa un iterabil fara a folosi un for
"""


def double(x):
    """Returneaza dublul valorii transmise ca parametru"""
    return 2*x


def pow2(x):
    return x**2


lista = [4, 7, 2, 10]

print(map(double, lista))   # obiect de tip map
print(list(map(double, lista)))
for value in map(double, lista):
    print(value)
doubles = map(double, lista)
print(type(doubles))

new_list = []
for element in lista:
    new_list.append(double(element))
print(f'Lista valorilor dublate: {new_list}')

m = map(pow2, [5, 6, 2])
print(f'Setul valorilor ridicate la puterea a doua: {set(m)}')
