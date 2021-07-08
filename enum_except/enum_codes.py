"""
Cream o enumerare in care sa stocam coduri de validare a unei valori introduse
de la tastatura
Codurile vor fi: INRANGE, TOOBIG, TOOSMALL
Valoarea introdusa: o zi a lunii
Vom verifica daca valoarea introdusa (ziua) este intre 1 si 31 si afisam codul
"""

from enum import Enum


class Codes(Enum):
    INRANGE = 1
    TOOSMALL = 2
    TOOBIG = 3


def main():
    for member in Codes:
        print(member.name, ' = ', member.value)
    try:
        day = int(input('Introduceti ziua: '))
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
    else:
        if day <= 31 and day >= 1:
            cod_validare = Codes.INRANGE
        elif day < 1:
            cod_validare = Codes.TOOSMALL
        else:
            cod_validare = Codes.TOOBIG

        print(f'Rezultatul validarii {day}: {cod_validare.name}')


if __name__ == '__main__':
    main()
