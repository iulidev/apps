"""
Inscrierea studentilor la un curs si urmarirea progresului
"""


class Student:
    """Creeaza obiecte de tip Student:
    Atribute:
        name - numele studentului
        age - varsta studentului
        lesson - lectia la care a ajuns (default 1)
    """

    def __init__(self, name, age, lesson=1):
        """Inscrierea la curs"""
        self.name = name
        self.age = age
        self.lesson = lesson

    def get_lesson(self):
        """Returneaza lectia la care a ajuns studentul"""
        return self.lesson

    def finish_lessons(self, no_lessons=1):
        """Inregistreaza progresul la curs, in raport cu ultima inregistrare
        Parameters:
        no_lessons - nr de lectii parcurse de la ultima inregistrare
        """
        self.lesson += no_lessons

    def info(self):
        print(f'Studentul {self.name}, age: {self.age}, lectie: {self.lesson}')


class Course:
    """Creeaza obiecte de tip curs
    Atribute:
        name - numele cursului
        max_studenti - capacitatea maxima a cursului
        total_lectii - nr de lectii din curs (static)
    """
    total_lectii = 15
    description = 'Curs programare in Python 3'

    def __init__(self, name, max_studenti):
        self.name = name
        self.max_studenti = max_studenti
        self.studenti = []

    def enrol_student(self, student):
        """Adauga / inscrie un student la curs
        Parametri:
            student - de tip Student, cu datele cursantului
        """
        if len(self.studenti) < self.max_studenti:
            self.studenti.append(student)
            print(f'Inscriere {student.name} realizata cu succes')
        else:
            print('Capacitatea maxima a cursului a fost atinsa')

    def get_max_capacity(self):
        """Returneaza numarul maxim de studenti care pot fi inscrisi"""
        return self.max_studenti

    def get_filled_capacity(self):
        """Returneaza numarul de studenti inscrisi la curs"""
        return len(self.studenti)

    @staticmethod
    def average(args):
        """Calculeaza media valorilor din lista transmisa ca parametru"""
        total = 0
        for value in args:
            total += value
        return total/len(args)

    def get_average_lesson(self):
        """Returneaza media lectiilor parcurse de studenti"""
        # total = 0
        # for student in self.studenti:
        #     total += student.lesson
        # return total / len(self.studenti)
        return Course.average([student.lesson for student in self.studenti])


def main():
    student1 = Student('John Doe', 20)
    student2 = Student('Alex Sima', 30, 2)
    student1.info()
    student1.finish_lessons(3)
    student1.info()
    student2.info()
    student2.finish_lessons()
    student2.info()
    curs = Course("Python developer", 3)
    curs.enrol_student(student1)
    curs.enrol_student(student2)
    curs.enrol_student(Student("Another Student", 29))
    print(f'Lectia medie este: {curs.get_average_lesson()}')
    print(f'Capacitatea maxima: {curs.get_max_capacity()}')
    student2.finish_lessons(4)
    print(f'Lectia medie este: {curs.get_average_lesson()}')
    student1.info()
    student2.info()
    student3 = Student("Max Max", 20)
    curs.enrol_student(student3)


if __name__ == "__main__":
    main()
