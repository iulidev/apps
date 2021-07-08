"""
Generator = o functie care produce o colectie de valori (o secventa de valori),
            una cate una (pe rand, si nu toate odata), la fiecare apelare se
            genereaza o noua valoare
yield - genereaza o noua valoare
next(obiect_generator) -    apelam generatorul pentru a produce / genera o noua
                            valoare (returneaza urmatoarea valoare generata)
Generator - iterator, este iterabil intr-o bucla for care poate expune toate
            valorile generate
Generator este similar unei functii care returneaza o colectie de valori,
        pe rand, dupa fiecare valoare intoarsa cu yield functia este pusa in
        asteptare pana la urmatoarea apelare, transferand controlul in program
        inapoi de unde a fost apelata
Avantaje:
    - nu genereaza toate valorile odata (performanta si viteza de calcul)
    - nu stocheaza toate valorile generate in memorie (management eficient al
    memoriei, mai ales cand lucram cu pachete de date foarte mari)
"""


def my_generator():
    value = 100
    yield value
    value += 100
    yield value
    value += 100
    yield value


def double(numbers):
    """
    Primeste ca parametru o lista de valori numbers
    Returneaza o lista cu valorile din numbers dublate
    """
    doubles = []
    for number in numbers:
        doubles.append(number * 2)
    return doubles


def double_generator(numbers):
    """Generator care genereaza dublul valorilor dintr-o lista
    """
    for number in numbers:
        yield number * 2


generator = my_generator()
print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
for value in generator:
    print(value)

my_numbers = [4, 7, 20, 1, 3]
print(f'Lista initiala: {my_numbers}')
print(f'Lista valorilor dublate: {double(my_numbers)}')

double_gen = double_generator(my_numbers)
print(f'Generatorul valorilor dublate: {double_gen}')
# print(next(double_gen))
# print(next(double_gen))
# print(next(double_gen))
for generated_value in double_gen:
    print('Valoare dublata:', generated_value)

values = [5, 66, 3, 2, 18]
double_values = [item*2 for item in values]
double_values_generator = (item*2 for item in values)   # comprehension
print(f'Valorile din lista {values} dublate cu list comprehension: '
      f'{double_values}')
print(f'Valorile din lista {values} dublate cu generator comprehension:')
for value in double_values_generator:
    print(value)

gen2 = (item * 2 for item in values)
new_list = list(gen2)
print(f'Lista obtinuta in urma conversiei obiectului de tip generator: '
      f'{new_list}')
