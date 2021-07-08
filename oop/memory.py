""" Memory allocation and garbage collection
In Python, memory management / allocation este realizat automat.
Memory allocation = mecanismul de alocare a memoriei cand rulam un program
Managementul memoriei prin:
- reference counting - contorizarea referintelor catre obiecte
- garbage collection = procesul prin care interpretorul elibereaza memoria si 
creeaza spatiu pentru alte obiecte
Functia id = identitatea unui obiect (adresa in memorie)
"""
import gc


x = 7  # creeaza un obiect in memorie de tip int, valoarea 7
y = 7  # obiectul este deja creat, o noua referinta este realizata prin
       # variabila y la acelasi obiect, avand aceeasi adresa de memorie
print(f'Adresa de memorie a obiectului referentiat de x: {id(x)}')
print(f'Adresa de memorie a obiectului referentiat de y: {id(y)}')
print(id(7))
print(f'x is y: {x is y}')
del x
# y = None
y = 4
print(f'Adresa in memorie a obiectului referentiat de y: {id(y)}')
print(f'GC threshold: {gc.get_threshold()}')
gc.collect()
