"""
Property decorator  - @property
                    - permite definirea unei metode si accesarea ca atribut
                    (o metoda a instantei poate fi decorata cu @property si
                    accesata ca atribut, fara paranteze)
"""


class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.fullname = f'{first} {last}'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, complete_name):
        self.first = complete_name.split(' ')[0]
        self.last = complete_name.split(' ')[1]
        # self.first, self.last = complete_name.split(' ')

    def info(self):
        print(f'{self.first} {self.last}, age {self.age}')


p = Person("Andrei", "Tomescu", 20)
p.info()
# print(f'Numele complet este: {p.fullname()}')
print(f'Numele complet este {p.fullname}')
p.fullname = "Alex Sima"    # e posibil assingment datorita @fullname.setter
p.info()
print(p.fullname)
print('Prenume: ', p.first)
