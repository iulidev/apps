"""
Polimorfism (Polymorphism)
In programare, polimorfism inseamna acelasi nume de functie (dar cu semnaturi
diferite = input si output posibil diferit) este folosit pentru tipuri diferite
de date
Polimorfism = abilitatea de a procesa obiecte in functie de tipul lor
Polimorfism (OOP) - a folosi acelasi nume de metoda in clase diferite
"""
from clase import Student, Cursant

numbers = [4, 6, 7]
curs = "Python developer"
print(f'Numarul de elemente din lista: {len(numbers)}')
print(f'Lungimea sirului de caractere: {len(curs)}')

cursant1 = Cursant()

student = Student("John Doe", 20)
persoane = []
persoane.append(cursant1)
persoane.append(student)
print(f'Lista persoane are {len(persoane)} elemente')
for persoana in persoane:
    persoana.info()
# help(Student)
x = Student('Max')
x.info()
