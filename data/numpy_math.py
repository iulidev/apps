"""
NumPy usability in math operations
(Utilizarea numpy in calcule matematice)
- realizeaza operatiile element cu element

    - numpy opereaza elementwise (element cu element)
    - aplica functii matematice fiecarui element din array (tablou)
Link:
https://numpy.org/doc/stable/reference/routines.math.html

"""

import numpy as np

ar = np.array([4, 7, 10, 20])
print(ar)
print(ar*3)
print(f'Radical din 16 este: {np.sqrt(16)}')
print('Functia sqrt (radical) aplicata unui array:')
print(np.sqrt(ar))
new_ar = np.array(([4, 10, 20, 12], [3, 14, 2, 1]))
print(new_ar)

print('Functia logartim aplicata unui array bidimensional')
print(np.log(new_ar))
print(np.cos(new_ar))
print('Functia ridicare la putere aplicata unui array unidimensional')
print(np.power(ar, 2))
b = np.linspace(2, 10, 9)
print(b)
c = np.arange(2, 11)
print(c)
b2 = np.linspace(2, 10, 20)
# dif_2_valori_consecutive = (stop-start)/(nr_elem-1)
print(b2)
b3 = np.linspace(2, 7, 10)
print(b3)
ar2 = np.arange(2, 9, 2)
print(ar)
print(ar2)
print('Aplicand multiply tablourilor ar si ar2:')
print(np.multiply(ar, ar2))
print(np.sin(ar))
print(f'Suma elementelor din ar: {ar.sum()}')
print(f'Suma elementelor din new_ar: {new_ar.sum()}')
print(new_ar)
print(f'Suma fiecarei coloane din new_ar: {new_ar.sum(axis=0)}')  # 0 - coloane
print(f'Suma fiecarei linii din new_ar: {new_ar.sum(axis=1)}')  # 1 - linii
