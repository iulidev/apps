"""
Lambda functions (lambda expressions) = functii anonime
Lambda function     = o functie anonima (nu are asociat un nume)
                    = o functie care primeste unul sau mai multe argumente si
                    are o singura expresie, pe baza careia se calculeaza
                    rezultatul
                    = returneaza un obiect de tip functie
Sintaxa:
    lambda argumente: expresie
O expresie lambda se poate referi si cu ajutorul unei variabile, situatie in
care se comporta ca o functie definita cu cuvantul cheie def
Avantaje:
    - readability
    - codul este concis
    - economie de memorie
"""


def square(x):
    """Intoarce patratul valorii transmise ca parametru
    """
    return x**2


print(f'Valoarea 4 ridicata la puterea a doua: {square(4)}')
print(f'Valoarea 4 ridicata la puterea a doua: {(lambda x: x**2)(4)}')

nums = [4, 2, 7]
m = map(square, nums)
print(f'Aplicam square elementelor din {nums}: {list(m)}')
# def patrat(x): return x**2
patrat = lambda x: x**2


print(f'Patratul lui 2: {patrat(2)}')
print(type(patrat))     # function object
m2 = map(patrat, nums)
print(f'Valorile listei {nums} ridicate la puterea a 2-a: {list(m2)}')
print(f'Valorile listei {nums} ridicate la puterea a 2-a: \
{list(map(lambda x: x**2, nums))}')

sum = lambda x, y: x+y
print(f'Suma valorilor {3} si {4}: {sum(3,4)}')

for value in nums:
    print(f"Paritate: {(lambda x: 'impar' if x % 2 == 1 else 'par')(value)}")

print(list(map(lambda a: 'impar' if a % 2 == 1 else 'par', nums)))
