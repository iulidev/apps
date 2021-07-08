""" Executia unui program cu parametri speciali
Modulul built-in sys
Implicit, la executie fiecare program are ca prim parametru
    calea si numele programului in sys.argv[0]
Pentru a transmite parametri se va folosi sys.argv[1], etc
"""
import sys


print('Executam un program cu parametri dati in linia de comanda')
print(f'Parametrul default {sys.argv[0]}')
print(f'S-au transmis {len(sys.argv)-1} parametri in CLI')
for argument in sys.argv:
    print(f'Parametru: {argument}')
print()
for index in range(len(sys.argv)):
    print(f'Parametrul {index}: {sys.argv[index]}')
