"""
Eliminarea duplicatelor dintr-o lista
Se da o lista si se elimina elementele duplicate, obtinandu-se lista
elementelor unice
"""
lista = [4, 7, 10, 7, 9, 2, 1, 4, 0, 33, 7]

# Solutia 1 - parcurgere in for si verificare unicitate
lista_unice = []
for item in lista:
    if item not in lista_unice:
        lista_unice.append(item)

print(f'Lista initiala: {lista}')
print(f'Lista cu elemente unice: {lista_unice}')

# Solutia 2 - conversie la set si reconversie a setului la lista
new_set = set(lista)
print(f'Setul obtinut pe baza listei: {new_set}')
new_lista_unice = list(new_set)
print(f'Lista cu elemente unice obtinuta pe baza setului: {new_lista_unice}')
