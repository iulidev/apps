"""
Cream o clasa care sa grupeze, ca metode statice, functii de calcul
adunare
impartire
inmultire

Tratam exceptii cand apelam metodele clasei
"""


class Calcul:
    """Clasa pentru realizarea prin metode statice a unor calcule matematice
    """

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError as e:
            return e


def main():
    try:
        print(Calcul.add(3, 6))
        print(Calcul.divide(4, 8))
        # print(Calcul.add(2, '4'))
        print(Calcul.multiply('2', 'string oarecare'))
        print(Calcul.divide(3, 0))
    # except ZeroDivisionError as e:
    #     print(f'{e}')
    except TypeError as e:
        print(f'{e.__class__.__name__}: {e}')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')


if __name__ == '__main__':
    main()
