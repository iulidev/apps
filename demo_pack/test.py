"""
Pentru a crea package grupam modulele (calcule.py, hello.py) intr-un folder
In acelasi folder adaugam un fisier __init__.py
pentru a indica Python ca este un package
Pentru a import din package:
from nume_package.nume_modul import nume_functie
"""

from package_one.calcule import add, power
from package_one.hello import say_hello

print(add(4, 3))
say_hello('you')
print(power(5, 2))
