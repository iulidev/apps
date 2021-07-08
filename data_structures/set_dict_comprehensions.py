"""
Set and dictionary comprehensions
Comprehension   = un mod concis de a construi colectii de elemente (liste,
                seturi, dictionare, generatoare) pe baza altei colectii
                folosind o expresie si, optional, aplicand o conditie if.
Sintaxa list comprehension:
    lista_noua = [expresie for item in lista_veche if conditie]
Iterabil (iterable) = o colectie de elemente care poate fi parcursa intr-o
                    bucla for pentru a furniza fiecare element pe rand
                    - list, range, str, set, tuple, dict, etc
    lista_noua = [expresie for item in iterabil if conditie]

Set comprehension:
    set_nou = {expresie for item in iterabil if conditie}
Avantaje comprehension:
    - cod mai simplu, mai concis, mai readable
Comprehension - o alternativa la for mai concisa

Dictionary comprehension:
    dictionar_nou = {key:value for item in iterabil if conditie}

"""

numbers = [4, 7, 9, 0, 22, 9, 4, 9, 9, 11, 23, 6, 8]
lista_pare = [x for x in range(100) if x % 2 == 0]   # lista numerelor pare
# print(f'Lista numerelor pare pana la 100: {lista_pare}')

# Cream setul numerelor pare pe baza listei numbers cu for si alte instructiuni
set_pare = set()
for number in numbers:
    if number % 2 == 0:
        set_pare.add(number)
print(f'Setul obtinut prin parcurgerea cu for a listei: {set_pare}')

# Cream setul numerelor pare pe baza listei numbers cu set comprehension
set_pare_comprehension = {item for item in numbers if item % 2 == 0}
print(f'Setul obtinut prin set comprehension: {set_pare_comprehension}')
set_5 = {value for value in set_pare_comprehension if value > 5}
print(f'Setul valorilor mai mari ca 5 obtinut prin comprehension: {set_5}')
set_dublu_5 = {2 * value for value in set_pare_comprehension if value > 5}
print(f'Setul valorilor duble: {set_dublu_5}')

languages = ['Python', 'Java', 'PHP', 'Java', 'Python']
skills_set = {'Programming in ' + language for language in languages}
print(f'Setul skills: {skills_set}')

# generam un dictionar cu cheia egala cu numarul si valoarea egala cu dublul
# numarului daca numarul este impar, pe baza unei liste / set
dict_impare = {number: number*2 for number in numbers if number % 2 == 1}
print(f'Dictionarul numerelor impare obtinut prin comprehension: '
      f'{dict_impare}')
dict_patrate_impare = {number: number *
                       number for number in numbers if number % 2 == 1}
print(f'Dictionar patrate impare: {dict_patrate_impare}')

skills = {'coding': 'Python', 'seniority': 5, 'age': 33, 'tools': 'github'}

updated_skills = {key.title(): value for key, value in skills.items()}
print(f'Updated skills: {updated_skills}')

u_skills = {}
for key, value in skills.items():
    u_skills[key.title()] = value
print(f'Skills obtinut scriind cod explicit: {u_skills}')
