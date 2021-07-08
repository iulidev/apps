"""

"""


class Employee:
    def __init__(self, name, age, salary, data_angajare=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.data_angajare = data_angajare

    def __str__(self):
        return (f'{__class__.__name__}({self.name}, {self.age}, '
                f'{self.salary}, {self.data_angajare})')

    def __add__(self, other):
        """
        Operatorul + determina suma salariilor
        Aplicat asupra a doua obiecte ale clasei
        """
        return self.salary + other.salary

    def display(self):
        print(f'{self.name}, {self.age}, {self.salary}')

    @classmethod
    def date_from_separate_values(cls, name, age, salary, month, day, year):
        # data_ang = str(month) + '/'+str(day)+'/' + str(year)
        # data_ang = '/'.join([str(month), str(day), str(year)])
        data_ang = '/'.join([str(value) for value in [month, day, year]])
        return cls(name, age, salary, data_ang)

    @property
    def experience(self):
        if self.data_angajare is not None:
            year_empl = self.data_angajare.split('/')[2]
            experience = 2021-int(year_empl)
            return experience
        else:
            return 'There is no employment date available'


class Developer(Employee):
    def __init__(
            self, name, age, salary, data_angajare=None, language='Python'):
        super().__init__(name, age, salary, data_angajare)
        self.language = language

    def __str__(self):
        return f'{__class__.__name__}({self.name}, {self.salary})'

    def show_language(self):
        print(f'Language:{self.language}')


def main():
    emp1 = Employee("John Doe", 45, 2000)
    # emp1.display()
    emp2 = Employee("Max Doe", 50, 4000, '04/20/2020')
    print(emp2)
    print(f'Aplicand operatorul + asupra a doi angajati: {emp1 + emp2}')
    print(emp1)
    # print(str(emp1))
    emp3 = Employee.date_from_separate_values(
        "Third Employee", 20, 4000, 5, 20, 2019)
    print(emp3)
    # print('Experienta in munca: ', emp3.get_experience())
    print('Experienta in munca: ', emp3.experience)
    dev = Developer('Developer Name', 25, 3000, '02/22/2018')
    print(dev)
    print(f'Experienta: {dev.experience}')


if __name__ == '__main__':
    main()
