""" Module in Python
Sunt doua moduri in care putem rula codul sursa:
1. ca script
    python program.py
2. ca modul, importand codul sursa
    import program
    2.1. in Python shell
    2.2. in alt program in Python
    Code reuse selectiv:
    program.nume_functie(parametri)
    module_name.nume_functie(parametri)
    2.3. Importam un modul redenumit
    import program as new_name
    sau:
    import module as new_name
    2.4. Import selectiv
    from module import nume_functie
    from module import nume_variabila
Variabila __name__ are valoarea __main__ cand rulam ca script
si valoare program (de exp calcule) cand importam ca module
In Python exista si module built-in: os, math, etc
Se importa cu acelasi statement:
    import os
"""

curs = "Python developer"
subiect = "Module in Python"


def square(value):
    """Returns the square of value
    """
    return value**2


def add(x, y):
    """Returns the sum of x and y
    """
    return x + y


def main():
    print(square(3))
    print(add(4, 2))


if __name__ == "__main__":
    main()
