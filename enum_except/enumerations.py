"""
Enum class
    - o clasa in Python pentru a crea enumerari
    Enumerare (enumeration) = un set de nume simbolice (numite membri) cu
    valori constante, unice daca aplicam decoratorul unique
    - concept similar unor variabile globale
    Avantaje:
        - grupa informatii
        - a beneficia de un mod de reprezentare standardizat
        - type-safety

Pentru a crea enumerari importam din libraria enum clasa Enum si o mostenim,
creand clase derivate
constante in Python - numele constantelor se scrie cu upper case
Atributele claselor derivate (enumerari):
- name
- value
Accesare membri:
- prin valoare (valoare)
- prin nume []
- iterativ intr-un for
"""
# class Nume_clase_derivata(Nume_clasa_de_baza):
from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    WHITE = 4


print(Color.RED.name)
print(Color.RED.value)
print(Color.WHITE.value)

for color in Color:
    print(color)
print(f'Membrul cu valoarea 3: {Color(3)}')
print(f'Membrul cu numele GREEN: {Color["GREEN"]}')

for color in Color:
    print(color.name, ': ', color.value)
