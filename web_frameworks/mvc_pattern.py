"""
MVC pattern in Python
MVC     - Model View Controller
https://ro.wikipedia.org/wiki/Model-view-controller
https://developer.mozilla.org/en-US/docs/Glossary/MVC

        - tipar arhitectural in software development (dezvoltarea de programe)
        - separa functionalitatile unei aplicatii (inclusiv aplicatie web)
        pentru a reduce complexitatea si a favoriza o mai usoara si eficienta
        colaborare a echipei de dezvoltare
        (software architectural design pattern)
        - separa aplicatia (functionalitatea) in trei componente:
        1/ Model
            - logica aplicatiei (prelucrarea datelor, reprezentarea interna a
            informatiei, incluzand comunicarea cu baza de date)
        2/ View
            - prezentarea catre utilizator a informatiilor sau interfata cu
            utilizatorul
        3/ Controller
            - gestioneaza cererile (requests) de la client catre aplicatie si
            comunica atat cu modelul pentru a obtine datele necesare cat si cu
            view-ul pentru prezentarea informatiei catre utilizator
 In Python, frameworkurile Flask si Django implementeaza MVC:
 Flask - partial, View si Contoller
 Djano - integral, Model, View, Controller cu mentiunea ca au denumiri diferite:
        Model este implementat prin Models
        View este implementat prin Templates
        Controller este implementat prin Views
        Django reflecta patternul MVC ca MTV (Model Template View)

"""
