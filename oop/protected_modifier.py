"""
Inheritance (Mostenirea)
Public (default) - membri accesibili de oriunde
Protected (_protected) - membri accesibili in interiorul package-ului
Private (__private) - membri accesibili doar in interiorul clasei

Membrii protected pot fi accesati:
- din interiorul clasei
- pot fi mosteniti de subclase si accesati la nivelul clasei derivate
cu sintaxa intanta._membru_protected
Conventie prin care limitam accesul la membrii protected doar la nivelul clasei
sau, prin motestenire, la nivelul subclasei.
Mecanismul implica accesul la un membru nu prin
instanta._membru_protected

ci definind o metoda care la randul ei se mosteneste de catre clasa derivata
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age     # protected
        self.salary = salary

    def info(self):
        print(f'{self.name}, varsta {self._age} cu salariu {self.salary}')

    def get_salary(self):
        return self.salary

    def get_age(self):
        return self._age


class Developer(Employee):
    def __init__(self, name, age, salary, language):
        # Employee.__init__(self, name, age, salary)
        super().__init__(name, age, salary)
        self.language = language

    def info(self):
        super().info()
        print(f'Language {self.language}')

    def extra_info(self):
        print(f'Sunt o instanta Developer {self.language}')

    def increment_age(self):
        self._age += 1


def main():
    emp = Employee("John Doe", 20, 2000)
    emp.info()
    print(f'Membrul protected age al instantei clasei Employee: '
          f'{emp.get_age()}')
    dev = Developer("Alex Sima", 30, 3000, 'Python')
    # dev.info()  # apelat metoda la nivelul insantei clasei derivate
    # dev.extra_info()
    print(f'Membrul protected age al instantei clasei derivate Developer: '
          f'{dev.get_age()}')
    # print(dev.salary)
    # help(Employee)
    # help(Developer)
    dev.info()
    dev.increment_age()
    dev.info()
    help(Developer)


if __name__ == '__main__':
    main()
