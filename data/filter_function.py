"""
Filter function (functie de filtrare)
    = filtreaza elementele unei colectii cu ajutorul unei functii data ca
    parametru
    = genereaza o colectie de elemente in care apar doar acele elemente din
    colectia initala pentru care functia este evaluata la True
Sintaxa:
    filter(functie, colectie)
Returneaza un obiect de tip filter, iterator - se poate itera peste cu for sau
realiza casting la un iterable (list, set, etc)
Colectia initiala transmisa ca parametru nu este schimbata (nu se schimba
starea colectiei data ca parametru functiei filter) - atat filter cat si map
sunt functii provenite din programarea functionala (prelucreaza colectii sau
date fara a le schimba starea, genereaza alte colectii sau date).

    filter(None, colectie)
        - genereaza o colectie cu elementele din colectia initiala data ca
        parametru care sunt evaluate boolean la True

"""


def este_par(x):
    """Intoarce True daca parametrul este par
    """
    return True if x % 2 == 0 else False


nums = [3, 7, 4, 2, 9, 10, 110, 22, 7]

lista_pare = []
for item in nums:
    if este_par(item):
        lista_pare.append(item)
print(f'Lista valorilor initiale: {nums}')
print(f'Lista filtrata prin for, daca valoarea este para: {lista_pare}')

lista_pare2 = filter(este_par, nums)
print(type(lista_pare2))
print(lista_pare2)
print(f'Lista filtrata prin filter, daca valoarea este para: \
{list(lista_pare2)}')
# for value in lista_pare2:
#     print(value, end=' ')
print(f'Lista initiala: {nums}')

numbers = [3, 4, 0, 5, 6, 0, "", False, "Python developer", True, 4.2]
print(f'Filter aplicat numbers fara functie: {list(filter(None, numbers))}')
print(numbers)
