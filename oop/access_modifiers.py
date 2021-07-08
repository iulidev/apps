"""
Access modifiers    - modificatori de acces
                    - schimba scope (domeniul de accesibilitate / vizibilitate) 
                    al unui membru (variabila sau metoda)
Implicit,   membrii clasei sunt publici,
            pot fi accesati de oriunde din afara clasei
Tipuri de modificatori:
1. Public (implicit)
2. Private  - membrul (variable/method) accesibil in interiorul clasei
            - este indicat ca private prin __ (prefixul dublu underscore)
3. Protected    - membrul (varible/method) accesibil in interiorul package
                - este setat ca protected prin _ (prefixul underscore)

"""

from clase import Angajat


e = Angajat("Ion Radu", 1000, 25)
print(e.nume)
e.arata_sal()
# print(e.__salariu)    # AttributeError - private
