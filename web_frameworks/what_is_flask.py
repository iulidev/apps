"""
Flask   - micro web framework (light-weight web application framework)
        - o colectie de librarii cu foarte putine dependente si nu necesita
        un setup foarte complex pentru a dezvolta aplicatii web

        Recomandare creare virtual environment inainte de instalare flask:
        Crearea de aplicatii web sa se realizeze intr-un mediu izolat, un
        virtual environment
        python -m venv nume_virtual_enviroment
        virtualenv nume_virtual_environment
        cream un mediu virtual

        Activare virtual environment:
        .\nume_mediu_virtual\Scripts\activate in Windows
        sau
        source nume_mediu_virtual\bin\activate

        Instalare:
        pip install flask
        Include modulele:
        Jinja2  - templating pentru front-end - UI
                - template inheritance (mostenire de sabloane)
        Werkzeug - modul care implementeaza un internal web server pentru test
        sau development cu ajutorul caruia aplicatiile web construite in flask
        se pot testa rapid, fara a fi necesar un alt web server
                - pe masina locala (localhost sau IP 127.0.0.1 ruleaza un server
                care primeste cererile de acces la aplicatie transmise in
                browser si mapate pe baza rutelor catre functii din aplicatie)
        Dezactivare:
        deactivate

        Pentru a crea o aplicatie web in Flask:
            - importam modulul flask, clasa Flask
            - instantiem clasa Flask
            - cream una sau mai multe rute (route)
                - asocieri intre un URL (adresa web) si un bloc de cod
                (o functie view)
            - rulata aplicatia flask
        WSGI    - Web Server Gateway Interface - protocol care permite
                comunicarea dintre web server si aplicatia web (instanta clasei
                Flask)

"""
# import flask
from flask import Flask
