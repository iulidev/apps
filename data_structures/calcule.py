"""
Calculator
Programul realizeaza operatii de calcul pe baza a doi operanzi si a unui
operator introdusi de la tastatura
operand1 operator operand2
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    return 'Impartire la zero!'     # y = 0


def floor_division(x, y):
    if y != 0:
        return x // y
    return 'Impartire la zero!'


operand1 = input('Operand1: ')
operator = input('Operator: ')
operand2 = input('Operand2: ')
# print(type(operand1))
operand1 = float(operand1)
operand2 = float(operand2)

calcule = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '//': floor_division
}
# print(calcule['*'])
functie_calcul = calcule.get(operator)
# if functie_calcul is not None:
#     print(f'Functia (calculul) care trebuie realizata: {functie_calcul}')
#     print(f'Rezultatul este: {functie_calcul(operand1, operand2)}')
# else:
#     print('Operatie necunoscuta')
print(
    'Operatie necunoscuta' if functie_calcul is None
    else f'Rezultatul este: {functie_calcul(operand1, operand2)}')
