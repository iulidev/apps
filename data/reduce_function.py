"""
Reduce() function
    = face parte din modulul built-in functools
    = primeste ca parametri o functie si o colectie de elemente (iterabil) si
    returneaza o valoare calculata cumulativ prin aplicarea functiei (data ca
    parametru, cu 2 argumente)

    Sintaxa:
    reduce(functie, colectie, valoare_initiala)

    from functools import reduce
Aplicarea functiei/expresiei lambda cu doua argumente, data ca prim parametru:
1. la prima iteratie se calculeaza acumulator = functie(element1, element2)
2. la a doua iteratie se calculcea acumulator = functie(acumulator, element3)

In cazul in care este transmis si al 3 lea parametru la prima iteratie se
calculeaza functie(valoare_initala, element1)
In ambele cazuri, se continua aplicarea functiei valorii anterioare a
acumulatorului si elementului curent pana la parcurgerea in intregime a
colectiei (iterabilului)

Functia reduce() reduce o colectie de elemente, iterabila, la o valoare
cu ajutorul unei functii sau expresii lambda
Primul argument al functiei este considerat acumulator, in el se va stoca
iterativ (cumulativ) la fiecare repetare valoarea obtinuta din aplicarea
functiei asupra valorii anterioare a acumulatorului si elementului curent
"""

from functools import reduce


def aduna(a, b):
    return a + b


def get_max(x, y):
    return x if x > y else y


numbers = [4, 6, 0, 9, 2]
suma = reduce(aduna, numbers)
print(f'Suma elementelor {numbers}: {suma}')
print(f'Suma elementelor {numbers} cu valoare initiala {100}: \
{reduce(aduna, numbers, 100)}')
print(f'Suma elementelor {numbers} cu valoare initiala {100}: \
{reduce(lambda x, y: x + y, numbers, 100)}')

countries = ['Romania', 'UK', 'Germania']
# reducem lista la suma lungimilor stringurilor
lungime_totala = reduce(lambda a, e: a + len(e), countries, 0)
# 0+len('Romania') la prima iteratie daca este data valoare initiala zero
# 'Romania'+len('UK') - TypeError fara valoare initiala
print(f'Lungimea totala, cumulata, a stringurilor din {countries}: '
      f'{lungime_totala}')
print(f'Maximul din {numbers} este :'
      f'{reduce(lambda a, e: a if a > e else e, numbers)}')
print(f'Maximul din {numbers} este: '
      f'{reduce(get_max, numbers)}')
print(f'Produsul elementelor {numbers}: {reduce(lambda a,e: a*e, numbers)}')
print(numbers)
